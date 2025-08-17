from django.db import models
from django.utils import timezone
#from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    stock = models.IntegerField(default=1)
    status = models.BooleanField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    product_image = models.ImageField(upload_to='photos/products', blank=True)

    def __str__(self):
        return self.name
