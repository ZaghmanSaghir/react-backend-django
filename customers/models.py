# Model is another name for database table

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    industry = models.CharField(max_length=100)
