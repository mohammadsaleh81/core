from django.db import models
from treebeard.mp_tree import MP_Node
from ckeditor_uploader.fields import RichTextUploadingField
from mobo.storage import PublicMediaStorage
from tools.uploader import upload_to_category, upload_to_brand
import uuid
from mobo.cache_backend import CachedManager

class TaxonomyBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.CharField(default=uuid.uuid4, editable=False, max_length=100)
    is_public = models.BooleanField(default=True)


    class Meta:
        unique_together = ('slug', 'organ')
        abstract = True


class Category(TaxonomyBaseModel, MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    title_fa = models.CharField(max_length=256, null=True, blank=True)
    nickname = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=2048, null=True, blank=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    content = RichTextUploadingField(null=True, blank=True)
    sku = models.CharField(max_length=6, null=True, blank=True)
    breadcrumbs = models.TextField(null=True, blank=True)  # Optional: replace with dynamic method
    has_sku = models.BooleanField(default=False)
    has_main = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, null=True, blank=True)
    svg_icon = models.TextField(null=True, blank=True)
    wp_id = models.CharField(max_length=12, null=True, blank=True)
    create_wp_page = models.BooleanField(default=False)
    multi_config = models.BooleanField(default=False)
    thumbnail = models.ImageField(
        storage=PublicMediaStorage(),
        upload_to=upload_to_category,
        blank=True, null=True,
    )
    organ = models.ForeignKey(
        "organization.Organization",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="categories"
    )

    node_order_by = ['order']


    def get_self_and_children(self):
        """
        Returns the current category along with all its children.
        """
        return list(self.get_descendants(include_self=True))


    def get_root_category(self):
        """
        Returns the root category of this category.
        """
        return self.get_root()


    @property
    def get_thumbnail_url(self):
        """
        Returns the URL of the thumbnail or a default placeholder.
        """
        return self.thumbnail.url if self.thumbnail else ''



    def get_configurations(self, key=None):
        configurations = self.get_root().configurations.all()
        if key:
            configurations = configurations.filter(key=key)
        return configurations


    def __str__(self):
        return self.title



class Brand(TaxonomyBaseModel):
    title = models.CharField(max_length=255, db_index=True)
    title_fa = models.CharField(max_length=256, null=True, blank=True)
    nickname = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=2048, null=True, blank=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    content = RichTextUploadingField(null=True, blank=True)
    sku = models.CharField(max_length=6, null=True, blank=True)
    wp_id = models.CharField(max_length=12, null=True, blank=True)
    create_wp_page = models.BooleanField(default=False)
    thumbnail = models.ImageField(
        storage=PublicMediaStorage(),
        upload_to=upload_to_brand,
        blank=True, null=True,
    )
    organ = models.ForeignKey(
        "organization.Organization",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="brands"
    )

    @property
    def get_thumbnail_url(self):
        """
        Returns the URL of the thumbnail or a default placeholder.
        """
        return self.thumbnail.url if self.thumbnail else ''

    def __str__(self):
        return self.title_fa




class Tag(TaxonomyBaseModel):
    title = models.CharField(max_length=250)
    title_fa = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.CharField(max_length=100, null=True, blank=True)
    wp_id = models.CharField(max_length=12, null=True, blank=True)
    create_wp_page = models.BooleanField(default=False)

    organ = models.ForeignKey(
        "organization.Organization",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="tags"
    )

    def __str__(self):
        return self.title_fa



class CategoryConfiguration(models.Model):
    """
    Represents the configuration structure for a category.
    Only root categories can directly define configurations.
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='configurations',
        help_text="The category this configuration is associated with. Must be a root category."
    )
    key = models.CharField(
        max_length=100,
        help_text="The configuration key (e.g., RAM, Storage, Color)."
    )
    input_type = models.CharField(
        max_length=50,
        choices=[
            ('text', 'Text'),
            ('number', 'Number'),
            ('boolean', 'Boolean'),
            ('dropdown', 'Dropdown'),
        ],
        help_text="The type of input for this configuration."
    )
    options = models.TextField(
        null=True,
        blank=True,
        help_text="Comma-separated options for dropdown input type (e.g., 4GB,8GB,16GB)."
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        unique_together = ('category', 'key')
        verbose_name = "Category Configuration"
        verbose_name_plural = "Category Configurations"

    def save(self, *args, **kwargs):
        # Check if the category is root
        if not self.category.is_root():
            raise ValueError("Configurations can only be added or modified for root categories.")
        super().save(*args, **kwargs)

        # Apply this configuration to all descendants of the category
        descendants = self.category.get_descendants()
        for descendant in descendants:
            if not CategoryConfiguration.objects.filter(category=descendant, key=self.key).exists():
                CategoryConfiguration.objects.create(
                    category=descendant,
                    key=self.key,
                    input_type=self.input_type,
                    options=self.options
                )

    def __str__(self):
        return f"{self.category.title} - {self.key}"
