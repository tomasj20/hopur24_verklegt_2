from django.db import models
from user.models import user_info
# Create your models here.

class cerealCategory(models.Model):
    name = models.CharField(max_length=255)

class cerealImage(models.Model):
    image = models.CharField(max_length=9999)
    path = models.CharField(max_length=1024)

class Cereal(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255, blank=True)
    quantity = models.IntegerField()
    description = models.CharField(max_length=1054, blank=True)
    category = models.ForeignKey(cerealCategory, on_delete=models.CASCADE)
    price = models.IntegerField()
    status = models.BooleanField(default=True, blank=True)
    discount = models.IntegerField(default=0, blank=True)
    total = models.IntegerField(blank=True, null=True)
    image = models.ForeignKey(cerealImage, on_delete=models.CASCADE)

    def get_total(self):
        self.total = self.price * ((100 - self.discount)/100)

    def __str__(self):
        return self.name

    def start(self):
        self.get_total()
        self.save()



class Cart(models.Model):
    currentID = models.CharField(max_length=999, blank=True, null=True)
    userInfo = models.ForeignKey(user_info, on_delete=models.DO_NOTHING, blank=True, null=True)
    shipping = models.CharField(max_length=50)

class CartProduct(models.Model):
    product_id = models.IntegerField(default=1)
    product_name = models.CharField(max_length=255, default="")
    prod_price = models.IntegerField()
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)

class Order(models.Model):
    total = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)





