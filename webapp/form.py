from django import forms
from webapp.models import Expense, ExpenseJan, ExpenseFeb
from webapp.models import UserData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"


class ExpenseFormJan(forms.ModelForm):
    class Meta:
        model = ExpenseJan
        fields = "__all__"


class ExpenseFormFeb(forms.ModelForm):
    class Meta:
        model = ExpenseFeb
        fields = "__all__"


class TestForm(forms.Form):
    name = forms.CharField(label="Enter name", max_length=30,
                           widget=forms.TextInput(attrs={
                               'id': 'fname',
                               'required': True,
                               'placeholder': 'Enter name',
                               'class': 'name'
                           }))
    email = forms.CharField(label="Enter email", max_length=30)


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class RegForm(forms.ModelForm):
    dob = forms.DateField(label='Date of Birth')
    choices = [('male', 'Male'), ('female', 'Female')]
    gender = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    class Meta:
        model = UserData
        fields = ('bio', 'gender', 'dob', 'location')
