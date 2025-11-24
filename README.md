# Ex02 Django ORM Web Application
# Date:24-11-2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
~~~
models.py
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

admins.py

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price','body_design','drive_type', 'fuel_type','seats','color','mileage')
~~~

# OUTPUT
![alt text](<../Select car to change _ Django site admin - Google Chrome 24-11-2025 20_04_48.png>)


# RESULT
Thus the program for creating a database using ORM hass been executed successfully
