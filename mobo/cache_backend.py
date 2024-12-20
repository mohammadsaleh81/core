import hashlib
import pickle
import redis
import time
from django.db.models.query import QuerySet
from django.conf import settings
import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache



logger = logging.getLogger('core.cache_queryset')

def get_cache_version(model_name):
    version = cache.get(f"cache_version:{model_name}")
    if version is None:
        version = 1
        cache.set(f"cache_version:{model_name}", version, None)
    return version

class CachedQuerySet(QuerySet):
    def _get_cache_timeout(self):
        model_name = self.model.__name__
        cache_config = getattr(settings, 'CACHE_CONFIG', {})
        timeout = cache_config.get(model_name, {}).get('timeout', 600)
        logger.debug(f"Cache timeout for {model_name}: {timeout}")
        return timeout

    def _generate_cache_key(self):
        query_string = str(self.query)
        hashed_query = hashlib.sha256(query_string.encode()).hexdigest()
        model_name = self.model.__name__
        version = get_cache_version(model_name)
        cache_key = f"query_cache:{model_name}:v{version}:{hashed_query}"
        logger.debug(f"Generated cache key: {cache_key}")
        return cache_key

    def __iter__(self):
        timeout = self._get_cache_timeout()
        if timeout is None:
            logger.debug("Cache is disabled for this model.")
            return super().__iter__()

        cache_key = self._generate_cache_key()
        logger.debug(f"Attempting to retrieve cache with key: {cache_key}")
        cached_result = cache.get(cache_key)

        if cached_result is not None:
            try:
                result = pickle.loads(cached_result)
                logger.info(f"Cache hit for key: {cache_key}")
                return iter(result)
            except Exception as e:
                logger.error(f"Error loading cache for key {cache_key}: {e}")

        redis_client = redis.StrictRedis.from_url(settings.CACHES['default']['LOCATION'])
        lock = redis_client.lock(f"lock:{cache_key}", timeout=10)
        acquired = lock.acquire(blocking=False)

        if acquired:
            try:
                logger.debug(f"Lock acquired for key: {cache_key}")
                result = list(super().__iter__())
                serialized_result = pickle.dumps(result)
                cache.set(cache_key, serialized_result, timeout=timeout)
                logger.info(f"Cache set for key: {cache_key}")
                return iter(result)
            finally:
                lock.release()
                logger.debug(f"Lock released for key: {cache_key}")
        else:
            logger.debug(f"Lock not acquired for key: {cache_key}, waiting for cache to be set.")
            for _ in range(10):
                time.sleep(0.1)
                cached_result = cache.get(cache_key)
                if cached_result is not None:
                    try:
                        result = pickle.loads(cached_result)
                        logger.info(f"Cache hit after waiting for key: {cache_key}")
                        return iter(result)
                    except Exception as e:
                        logger.error(f"Error loading cache for key {cache_key}: {e}")
            logger.warning(f"Cache not found after waiting for key: {cache_key}, executing query.")
            result = list(super().__iter__())
            serialized_result = pickle.dumps(result)
            cache.set(cache_key, serialized_result, timeout=timeout)
            logger.info(f"Cache set after waiting for key: {cache_key}")
            return iter(result)

    def __len__(self):
        cache_key = self._generate_cache_key()
        cached_result = cache.get(cache_key)
        if cached_result is not None:
            try:
                result = pickle.loads(cached_result)
                logger.debug(f"Cache hit for __len__ with key: {cache_key}")
                return len(result)
            except Exception as e:
                logger.error(f"Error loading cache for __len__ with key {cache_key}: {e}")
        return super().__len__()




from django.db import models
from .cache_backend import CachedQuerySet

class CachedManager(models.Manager):
    """
    Custom Manager to use the CachedQuerySet.
    """
    def get_queryset(self):
        return CachedQuerySet(self.model, using=self._db)




@receiver(post_save)
@receiver(post_delete)
def invalidate_model_cache(sender, **kwargs):
    """
    Increments the cache version for the model when data changes.
    """
    model_name = sender.__name__
    logger.debug(f"Invalidating cache for model: {model_name}")
    try:
        cache.incr(f"cache_version:{model_name}")
        logger.debug(f"Cache version incremented for model: {model_name}")
    except ValueError:
        cache.set(f"cache_version:{model_name}", 1, None)
        logger.debug(f"Cache version set to 1 for model: {model_name}")
