from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    publish_year = models.IntegerField(null=True)
    num_of_page = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    sold = models.IntegerField(null=True)
    cover = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"