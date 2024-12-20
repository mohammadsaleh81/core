from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage():
    pass
    """
    Storage backend for managing static files on AWS S3.
    """
    location = ''  # Location in the S3 bucket
    default_acl = 'public-read'  # Public access to static files


class PublicMediaStorage(S3Boto3Storage):
    """
    Storage backend for managing public media files on AWS S3.
    Files uploaded here will be accessible via public URLs.
    """
    location = settings.AWS_PUBLIC_MEDIA_LOCATION  # Location in the S3 bucket
    default_acl = 'public-read'  # Public access to media files
    file_overwrite = False  # Prevent overwriting files with the same name


class PrivateMediaStorage(S3Boto3Storage):
    """
    Storage backend for managing private media files on AWS S3.
    Files uploaded here will require a presigned URL for access.
    """
    location = settings.AWS_PRIVATE_MEDIA_LOCATION  # Location in the S3 bucket
    default_acl = 'private'  # Private access for files
    file_overwrite = False  # Prevent overwriting files with the same name
    custom_domain = False  # Disable custom domain for private files
