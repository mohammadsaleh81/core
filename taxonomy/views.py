from rest_framework.views import APIView
from rest_framework.response import Response
from tools.paginations import StandardResultsPagination
from tools.mixins import OrganizationMixin
from taxonomy.serializers import (
    CategorySerializer,
    BrandSerializer,
    TagSerializer,
)
from taxonomy.selectors import (
    get_root_categories,
    get_category,
    get_child_categories_by_id,
    get_brands,
    get_brand_by_id,
    get_tags
    )

from django.core.cache import cache

class CategoryListView(APIView, OrganizationMixin):
    """
    API View to list categories, optionally filtered by parent_id.
    """
    def get(self, request, *args, **kwargs):
        organization = self.get_organization()
        cache.set('categories', 'ccccccccccccc', 333)
        parent_id = request.query_params.get('parent_id')
        if parent_id:
            categories = get_child_categories_by_id(parent_id, organization)

        else:
            categories = get_root_categories(organization)

        # Apply pagination
        paginator = StandardResultsPagination()
        paginated_categories = paginator.paginate_queryset(categories, request)
        serializer = CategorySerializer(paginated_categories, many=True)

        return paginator.get_paginated_response(serializer.data)


class CategoryDetailView(APIView, OrganizationMixin):
    """
    API View to fetch details of a single category.
    """
    def get(self, request, id, *args, **kwargs):
        organization = self.get_organization()

        category = get_category(id, organization)
        if not category:
            return Response({"detail": "Category not found."}, status=404)

        serializer = CategorySerializer(category)
        return Response(serializer.data)


class BrandListView(APIView, OrganizationMixin):
    """
    API View to list brands filtered by organization.
    """
    def get(self, request, *args, **kwargs):
        organization = self.get_organization()

        brands = get_brands(organization)
        paginator = StandardResultsPagination()
        paginated_brands = paginator.paginate_queryset(brands, request)
        serializer = BrandSerializer(paginated_brands, many=True)

        return paginator.get_paginated_response(serializer.data)


class BrandDetailView(APIView, OrganizationMixin):
    """
    API View to retrieve details of a specific brand.
    """
    def get(self, request, id, *args, **kwargs):
        organization = self.get_organization()

        brand = get_brand_by_id(organization, id)
        if not brand:
            return Response({"detail": "Brand not found."}, status=404)

        serializer = BrandSerializer(brand)
        return Response(serializer.data)


class TagListView(APIView, OrganizationMixin):
    """
    API View to list tags filtered by organization.
    """
    def get(self, request, *args, **kwargs):
        organization = self.get_organization()

        tags = get_tags(organization)
        paginator = StandardResultsPagination()
        paginated_tags = paginator.paginate_queryset(tags, request)
        serializer = TagSerializer(paginated_tags, many=True)

        return paginator.get_paginated_response(serializer.data)

