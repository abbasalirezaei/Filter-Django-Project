from django.db import models
from django.urls import reverse

# Simple Product Model


class Product(models.Model):
    """
        This the Simple Product model Just for show the filter and you can customize it
    """
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='products/')
    content = models.TextField(max_length=1000)
    price = models.FloatField()

    class Meta:
       
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


    # get_absolute_url will return url from product
    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            "pk" : self.pk
        
        })