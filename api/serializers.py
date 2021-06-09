from rest_framework import serializers
from store import models as store_models
from website import models as website_models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = store_models.Product
        fields = '__all__'
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = store_models.Category
        fields = '__all__'


class BigCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = store_models.BigCategory
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = website_models.Banner
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = website_models.Contact
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = website_models.About
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = website_models.Location
        fields = '__all__'


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = website_models.Newsletter
        fields = '__all__'