from django.contrib import admin
from webapp.models import Expense, ExpenseJan, ExpenseFeb, ExpenseMar, ExpenseApr, ExpenseMay, ExpenseJun, ExpenseJul, ExpenseAug, ExpenseSep, ExpenseOct, ExpenseNov, ExpenseDec
from webapp.models import UserData

# Register your models here.
admin.site.register(Expense)
admin.site.register(ExpenseJan)
admin.site.register(ExpenseFeb)
admin.site.register(ExpenseMar)
admin.site.register(ExpenseApr)
admin.site.register(ExpenseMay)
admin.site.register(ExpenseJun)
admin.site.register(ExpenseJul)
admin.site.register(ExpenseAug)
admin.site.register(ExpenseSep)
admin.site.register(ExpenseOct)
admin.site.register(ExpenseNov)
admin.site.register(ExpenseDec)
admin.site.register(UserData)
