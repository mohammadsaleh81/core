from rest_framework import serializers
from taxonomy.models import Category, CategoryConfiguration


class CategoryConfigurationSerializer(serializers.ModelSerializer):
    """
    Serializer for CategoryConfiguration model.
    """
    class Meta:
        model = CategoryConfiguration
        fields = ['key', 'input_type', 'options']


class ChildCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for child categories using django-treebeard's MP_Node.
    """
    childs = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'title_fa', 'slug', 'childs']


    def get_childs(self, obj):
        """
        Fetch child categories for this category.
        """
        children = obj.get_children()
        return ChildCategorySerializer(children, many=True).data


class RootCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for root categories, including child categories and configurations.
    """
    configurations = serializers.SerializerMethodField()
    childs = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'title_fa', 'slug', 'configurations', 'childs']

    def get_configurations(self, obj):
        """
        Fetch configurations for the root category.
        """
        configurations = obj.get_configurations()
        return CategoryConfigurationSerializer(configurations, many=True).data

    def get_childs(self, obj):
        """
        Fetch child categories for the root category.
        """
        children = obj.get_children()
        return ChildCategorySerializer(children, many=True).data


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.
    Includes its configurations and parent/children relationships.
    """
    configurations = serializers.SerializerMethodField()
    parent = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'title_fa', 'slug', 'description', 'parent', 'configurations']

    def get_configurations(self, obj):
        """
        Fetch configurations for the category.
        """
        configurations = obj.get_configurations()
        return CategoryConfigurationSerializer(configurations, many=True).data


from rest_framework import serializers
from taxonomy.models import Brand, Tag


class BrandSerializer(serializers.ModelSerializer):
    """
    Serializer for Brand model.
    """

    class Meta:
        model = Brand
        fields = [
            'id', 'title', 'title_fa', 'nickname', 'description',
            'slug', 'content', 'sku', 'wp_id', 'create_wp_page',

        ]


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for Tag model.
    """
    class Meta:
        model = Tag
        fields = [
            'id', 'title', 'title_fa', 'slug', 'description',
            'wp_id', 'create_wp_page'
        ]
