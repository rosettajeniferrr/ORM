from django.db import models
from django.contrib import admin

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.FloatField()
    body_design = models.CharField(max_length=100)
    drive_type = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    seats = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.FloatField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price','body_design','drive_type', 'fuel_type','seats','color','mileage')



