from django.db import models


# Created Employee Model and provided name, empid and city Field.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    empid = models.IntegerField()
    city = models.CharField(max_length=50)
