from django.db import models
from django.core.validators import MinValueValidator


class Collection(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    collections = models.ManyToManyField(
        "Collection",
        blank=True
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    calories = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title
