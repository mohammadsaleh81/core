from rest_framework import serializers
from product.models import Product, ProductVariant, ProductConfiguration
from taxonomy.models import Category, Brand, CategoryConfiguration


class ProductConfigurationSerializer(serializers.ModelSerializer):
    """
    Serializer for ProductConfiguration model.
    Includes configuration key and its value.
    """
    configuration_key = serializers.CharField(source='configuration.key')

    class Meta:
        model = ProductConfiguration
        fields = ['configuration_key', 'value']


class ProductVariantSerializer(serializers.ModelSerializer):
    """
    Serializer for ProductVariant model.
    Includes its configurations.
    """
    configurations = ProductConfigurationSerializer(many=True, read_only=True)

    class Meta:
        model = ProductVariant
        fields = ['sku', 'price', 'is_active', 'configurations']


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.
    Includes variants and their configurations.
    """
    # category = serializers.CharField(source='category.title')
    # brand = serializers.CharField(source='brand.title', allow_null=True)
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'title_fa', 'slug', 'category', 'brand', 'min_price', 'max_price', 'variants']


class CategoryConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryConfiguration
        fields = ['key', 'input_type', 'options']

class CategorySerializer(serializers.ModelSerializer):
    configurations = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'configurations']

    def get_configurations(self, obj):
        return CategoryConfigurationSerializer(obj.get_effective_configurations(), many=True).data
