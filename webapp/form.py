from django import forms
from webapp.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"
