from django.contrib import admin
from product.models import Product, ProductVariant, ProductConfiguration
from taxonomy.models import Category, Brand
from unfold.admin import ModelAdmin



class ProductConfigurationInline(admin.TabularInline):
    """
    Inline admin for managing configurations of a product variant.
    """
    model = ProductConfiguration
    extra = 1  # Number of empty forms to show
    fields = ('configuration', 'value')  # Fields to display
    autocomplete_fields = ['configuration']  # Enable auto-completion for configurations


class ProductVariantInline(admin.TabularInline):
    """
    Inline admin for managing product variants.
    """
    model = ProductVariant
    extra = 1  # Number of empty forms to show
    fields = ('sku', 'price', 'is_active')  # Fields to display
    readonly_fields = ('sku',)  # SKU should be read-only
    inlines = [ProductConfigurationInline]  # Nested Inline for variant configurations


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin for managing products with inline variants and configurations.
    """
    list_display = ('title', 'category', 'brand', 'min_price', 'max_price','status', 'is_configurable',  'updated_at')

    list_editable = ('status',)  # Allow inline editing
    list_filter = ('status', 'brand')  # Filters in the sidebar
    search_fields = ('title', 'slug', 'nickname', 'upc')
    autocomplete_fields = ['category', 'brand', 'tags']
    inlines = [ProductVariantInline]  # Inline for managing variants
    fieldsets = (
        (None, {
            'fields': ('title', 'title_fa', 'slug', 'nickname', 'thumbnail', 'content', 'summery')
        }),
        ('Pricing', {
            'fields': ('min_price', 'max_price')
        }),
        ('Status & Configuration', {
            'fields': ('status', 'is_configurable', 'mobo_offer', 'crawler_status', 'generate_content_ai')
        }),
        ('Relations', {
            'fields': ('category', 'brand', 'tags')
        }),
    )
    readonly_fields = ('updated_at', 'created_at')  # Make these fields read-only



@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    """
    Admin for managing product variants directly.
    """
    list_display = ('product', 'sku', 'price', 'is_active')
    list_filter = ('product', 'is_active')
    search_fields = ('sku', 'product__title')
    autocomplete_fields = ['product']


@admin.register(ProductConfiguration)
class ProductConfigurationAdmin(admin.ModelAdmin):
    """
    Admin for managing product configurations directly.
    """
    list_display = ('variant', 'configuration', 'value')
    list_filter = ('variant__product', 'configuration__category', 'configuration__key')
    search_fields = ('variant__sku', 'configuration__key', 'value')
    autocomplete_fields = ['variant', 'configuration']
