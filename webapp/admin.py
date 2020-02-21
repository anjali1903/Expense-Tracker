from django.contrib import admin
from webapp.models import Expense, ExpenseJan, ExpenseFeb
from webapp.models import UserData

# Register your models here.
admin.site.register(Expense)
admin.site.register(ExpenseJan)
admin.site.register(ExpenseFeb)
admin.site.register(UserData)
