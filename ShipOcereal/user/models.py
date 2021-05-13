from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

class user_info(models.Model):
    full_name = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    town = models.CharField(max_length=100)
    profile_image = models.CharField(max_length=9999)
    country = models.ForeignKey(country, on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)


class SearchHistory(models.Model):
    search = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


