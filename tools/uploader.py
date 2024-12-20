import os
from uuid import uuid4

def upload_to_folder(instance, filename, folder_name):
    """
    Generate a dynamic file path for uploaded files.
    """
    _, ext = os.path.splitext(filename)
    return f"{folder_name}/{uuid4()}{ext}"

def upload_to_category(instance, filename):
    return upload_to_folder(instance, filename, "category")

def upload_to_brand(instance, filename):
    return upload_to_folder(instance, filename, "brand")


def upload_to_product(instance, filename):
    return upload_to_folder(instance, filename, "product")
