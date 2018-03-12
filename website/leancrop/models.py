from django.db import models
# from rest_framework import serializers

# Create your models here.



class Farmerdata(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField(default=0)
    language = models.CharField(max_length=200)

    # class Meta:
    #     db_table = "farmerdata"

    def __str__(self):
        return self.name


class Farmdata(models.Model):
    farmer = models.ForeignKey('Farmerdata', on_delete=models.CASCADE, related_name="fd")
    area = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    crop_grown = models.CharField(max_length=200)
    sowing_date = models.DateField('sowing date')
    coordinates_array = models.IntegerField(default=0)

    # class Meta:
    #     db_table = "farmdata"

    def __str__(self):
        return self.crop_grown


class Scheduledata(models.Model):

    farmer = models.ForeignKey('Farmerdata', on_delete=models.CASCADE, related_name="sd")
    farm = models.ForeignKey('Farmdata', on_delete=models.CASCADE, related_name="fm", default=0)
    days_after = models.IntegerField(default=0)
    fertiliser = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    quantity_unit = models.CharField(max_length=200)

    # class Meta:
    #     db_table = "scheduledata"

    def __str__(self):
        return self.fertiliser

