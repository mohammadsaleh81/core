from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product
from .serializers import ProductSerializer, CategorySerializer
from taxonomy.models import Category, CategoryConfiguration



class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all().select_related()  # Fetch all products
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)



class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data
        return Response(data)
