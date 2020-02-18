from django.db import models

# Create your models here.


class Expense(models.Model):
    date = models.DateField()
    expense = models.CharField(max_length=30)
    price = models.IntegerField()
