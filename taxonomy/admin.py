from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from taxonomy.models import Category, Brand, Tag, CategoryConfiguration


class CategoryConfigurationInline(admin.TabularInline):
    """
    Inline configuration for categories.
    """
    model = CategoryConfiguration
    extra = 1  # Number of empty forms to display
    fields = ('key', 'input_type', 'options')  # Fields to display in the inline form


@admin.register(Category)
class CategoryAdmin(TreeAdmin):
    """
    Admin for Category with tree structure management.
    """
    form = movenodeform_factory(Category)  # Enable drag-and-drop for tree structure
    list_display = ('title', 'slug', 'is_public', 'organ', 'order', 'updated_at')
    list_filter = ('is_public', 'organ')
    search_fields = ('title', 'slug', 'title_fa', 'description')
    ordering = ['order']
    inlines = [CategoryConfigurationInline]  # Inline configurations

    fieldsets = (
        (None, {
            'fields': ('title', 'title_fa', 'nickname', 'slug', 'description', 'is_public', 'order')
        }),
        ('Content', {
            'fields': ('content', 'svg_icon', 'thumbnail')
        }),
        ('Advanced', {
            'fields': ('sku', 'breadcrumbs', 'wp_id', 'create_wp_page', 'multi_config', 'organ')
        }),
    )



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    Admin for Brand management.
    """
    list_display = ('title', 'slug', 'is_public', 'organ', 'updated_at')
    list_filter = ('is_public', 'organ')
    search_fields = ('title', 'title_fa', 'nickname', 'description')
    ordering = ['title']



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Admin for Tag management.
    """
    list_display = ('title', 'slug', 'is_public', 'organ', 'updated_at')
    list_filter = ('is_public', 'organ')
    search_fields = ('title', 'title_fa', 'description')
    ordering = ['title']



@admin.register(CategoryConfiguration)
class CategoryConfigurationAdmin(admin.ModelAdmin):
    """
    Admin for managing category configurations.
    """
    list_display = ('category', 'key', 'input_type', 'options')
    list_filter = ('category', 'input_type')
    search_fields = ('key', 'options')
    ordering = ('category', 'key')