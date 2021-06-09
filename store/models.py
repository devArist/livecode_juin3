from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.FileField(upload_to='img')
    name = models.CharField(max_length=200, verbose_name='nom')
    price = models.FloatField(verbose_name='prix')
    categories = models.ManyToManyField("Category", verbose_name='catégories')
    big_category = models.ManyToManyField(
        "BigCategory", 
        verbose_name="grandes catégories",
        )
    number_in_stock = models.IntegerField(verbose_name='nombre de ce produit en stock')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'produit'


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='nom')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Catégorie'


class BigCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='nom')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'grande catégorie'
        verbose_name_plural = 'grandes catégories'