from django.db import models

# Create your models here.


class Catagory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    Catagory = models.ForeignKey(Catagory,  on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True, default=0.00)
    stock = models.PositiveIntegerField(blank=True, null=True)
    discount_price = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='Product_Image/', blank=True, null=True, default='defaultimage.png')


    def __str__(self):
        return self.name