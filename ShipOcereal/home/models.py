from django.db import models

# Create your models here.
class cerealCategory(models.model):
    name = models.CharField(max_length=255)


class Cereal(models.model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(cerealCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    inStock = models.BooleanField()
    onSale = models.BooleanField()

class cerealImage(models.model):
    image = models.CharField(max_length = 9999)
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)

