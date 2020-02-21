from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your models here.


class Expense(models.Model):
    month = models.CharField(max_length=15, default='')
    date = models.IntegerField()
    expense = models.CharField(max_length=30)
    price = models.IntegerField()


class ExpenseJan(models.Model):
    date = models.IntegerField()
    expense = models.CharField(max_length=30)
    price = models.IntegerField()


class ExpenseFeb(models.Model):
    date = models.IntegerField()
    expense = models.CharField(max_length=30)
    price = models.IntegerField()


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=30)
    dob = models.DateField()
    location = models.CharField(max_length=30)
