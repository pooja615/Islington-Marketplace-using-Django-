from django.db import models


class cart(models.Model):
    cart_id= models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id

# Create your models here.
