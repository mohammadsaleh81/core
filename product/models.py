import uuid
from mobo.storage import PublicMediaStorage
from tools.uploader import upload_to_product
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from mobo.cache_backend import CachedManager

class ProductBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.CharField(default=uuid.uuid4, unique=True, max_length=100)

    # objects = CachedManager()
    class Meta:
        abstract = True


class Product(ProductBaseModel):
    AVIALABLE_CHOICES = {
        ("avail", 'موجود در ایران'),
        ("notavail", 'ناموجود در ایران'),
        ("tobeavail", 'به زودی موجود'),
        ("cancelled", 'توقف تولید'),
    }
    status = models.CharField(max_length=15, choices=AVIALABLE_CHOICES, default='avail')
    title = models.CharField(max_length=128)
    title_fa = models.CharField(max_length=256)
    thumbnail = models.ImageField(storage=PublicMediaStorage(), upload_to=upload_to_product, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=128)
    brand = models.ForeignKey("taxonomy.Brand", on_delete=models.CASCADE, related_name='products', null=True)
    min_price = models.DecimalField(max_digits=19, decimal_places=4, default=0.0000)
    max_price = models.DecimalField(max_digits=19, decimal_places=4, default=0.0000)
    content = RichTextUploadingField(null=True, blank=True)
    summery = RichTextUploadingField(null=True, blank=True)
    tags = models.ManyToManyField('taxonomy.Tag', null=True, blank=True)
    upc = models.CharField(max_length=120, null=True, blank=True)
    has_wp_page = models.BooleanField(default=False)
    extra = models.TextField(null=True, blank=True)
    nickname = models.CharField(max_length=600, null=True, blank=True)
    category = models.ForeignKey("taxonomy.Category", on_delete=models.CASCADE, related_name='accessories', null=True, blank=True)
    generate_content_ai = models.BooleanField(default=False)
    organ = models.ForeignKey("organization.Organization", on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    wp_post_id = models.CharField(max_length=10, null=True)
    mobo_offer = models.BooleanField(default=False)
    edit_upc_access = models.BooleanField(default=True)
    crawler_status = models.BooleanField(default=True)
    is_configurable = models.BooleanField(default=False)


    def get_configuration(self, key):
        config = self.configurations.filter(configuration__key=key).first()
        return config.value if config else None

    def get_all_configurations(self):
        """
        Get all configurations for this product as a dictionary.
        :return: A dictionary of configurations {key: value}.
        """
        return {
            config.configuration.key: config.value
            for config in self.configurations.all()
        }

    def __str__(self):
        return self.title



class ProductConfiguration(models.Model):
    """
    Stores the values for a variant's configurations based on the category configuration.
    """
    variant = models.ForeignKey(
        'ProductVariant',
        on_delete=models.CASCADE,
        related_name='configurations',
        null=True
    )

    configuration = models.ForeignKey(
        "taxonomy.CategoryConfiguration",
        on_delete=models.CASCADE,
        related_name='product_values'
    )
    value = models.CharField(max_length=255)  # Value of the configuration (e.g., 16GB, Red)

    def __str__(self):
        return f"{self.variant}: {self.value}"



class ProductVariant(models.Model):
    """
    Represents a variant of a product (e.g., RAM=4GB, Storage=128GB).
    """
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='variants'
    )
    price = models.DecimalField(max_digits=19, decimal_places=4, default=0.0000)
    sku = models.CharField(max_length=50, unique=True)  # SKU for the variant
    is_active = models.BooleanField(default=True)  # Whether this variant is available

    def __str__(self):
        return f"{self.product.title} - Variant {self.id}"
