from . import serializers
from store import models as store_models
from website import models as website_models
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = store_models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = store_models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class BigCategoryViewSet(viewsets.ModelViewSet):
    queryset = store_models.BigCategory.objects.all()
    serializer_class = serializers.BigCategorySerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = website_models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset = website_models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = website_models.About.objects.all()
    serializer_class = serializers.AboutSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = website_models.Location.objects.all()
    serializer_class = serializers.LocationSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = website_models.Newsletter.objects.all()
    serializer_class = serializers.LocationSerializer