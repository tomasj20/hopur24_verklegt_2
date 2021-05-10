from django.db import models
from user.models import user_info
# Create your models here.

class cerealCategory(models.Model):
    name = models.CharField(max_length=255)

class Cereal(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(cerealCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    inStock = models.BooleanField()
    onSale = models.FloatField(default=0, blank=True)
    total = models.IntegerField(blank=True, null=True)

    def calculate_total(self):
        self.total = self.price * ((100 - self.onSale)/100)

    def __str__(self):
        return self.name

    def start(self):
        self.calculate_total()
        self.save()

class cerealImage(models.Model):
    image = models.CharField(max_length=9999)
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)

class Cart(models.Model):
    cartID = models.CharField(max_length=999, blank=True, null=True)
    userInfo = models.ForeignKey(user_info, on_delete=models.DO_NOTHING, blank=True, null=True)
    shipping = models.CharField(max_length=50)

class CartProduct(models.Model):
    product_id = models.IntegerField(default=1)
    product_name = models.CharField(max_length=255, default="")
    quantity = models.IntegerField()
    prod_price = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)

class Order(models.Model):
    total = models.FloatField()
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)



