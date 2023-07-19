from django.shortcuts import render
from rest_framework import generics
from .models import CatShop
from .serializers import CatShopSerializer

# Create your views here.
class CatShopList(generics.ListCreateAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatShopSerializer

class CatShopDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatShopSerializer