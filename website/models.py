from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(max_length=200, verbose_name='email')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'newsletter'


class Banner(models.Model):
    image = models.FileField(upload_to='img')
    title = models.CharField(max_length=200, verbose_name='titre')
    description = HTMLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'bannière'


class About(models.Model):
    image = models.FileField(upload_to='img')
    title = models.CharField(max_length=200, verbose_name='titre')
    description = HTMLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'A propos'
        verbose_name_plural = 'A propos'


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='nom')
    email = models.EmailField(max_length=200, verbose_name='email')
    subject = models.CharField(max_length=200, verbose_name='sujet')
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class Location(models.Model):
    name = models.CharField(max_length=200, verbose_name='nom de l\'emplacement')
    address = models.CharField(max_length=200, verbose_name='adresse')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'emplacement'


class HeaderTitle(models.Model):
    title = models.CharField(max_length=200, verbose_name='titre')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'titre de l\'en-tête'
        verbose_name_plural = 'titre de l\'en-tête'