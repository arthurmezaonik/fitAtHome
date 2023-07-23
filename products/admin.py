from django.contrib import admin
from .models import Collection, Product

class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'sku',
        'collection',
        'price',
        'calories',
        'image',
    )

    ordering = ('title',)

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Product, ProductAdmin)
