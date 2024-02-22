from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "publish_year", "num_of_page", "price", "sold", "stock", "cover", "description")

admin.site.register(Product, ProductAdmin)