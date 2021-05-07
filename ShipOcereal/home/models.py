from django.db import models

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
    image = models.ManyToManyField(image)

    def calculate_total(self):
        self.total = self.price * ((100 - self.discount)/100)

class cerealImage(models.Model):
    image = models.CharField(max_length=9999)
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)

