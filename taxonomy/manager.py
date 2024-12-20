from django.db import models

class CategoryQuerySet(models.QuerySet):
    def for_organization(self, organ):
        return self.filter(organ=organ)

    def public(self):
        return self.filter(is_public=True)

class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def for_organization(self, organ):
        return self.get_queryset().for_organization(organ)

    def public(self):
        return self.get_queryset().public()
