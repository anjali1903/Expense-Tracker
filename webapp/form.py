from django import forms
from webapp.models import Expense, ExpenseJan, ExpenseFeb, ExpenseMar, ExpenseApr, ExpenseMay, ExpenseJun, ExpenseJul, ExpenseAug, ExpenseSep, ExpenseOct, ExpenseNov, ExpenseDec
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


class ExpenseFormMar(forms.ModelForm):
    class Meta:
        model = ExpenseMar
        fields = "__all__"


class ExpenseFormApr(forms.ModelForm):
    class Meta:
        model = ExpenseApr
        fields = "__all__"


class ExpenseFormMay(forms.ModelForm):
    class Meta:
        model = ExpenseMay
        fields = "__all__"


class ExpenseFormJun(forms.ModelForm):
    class Meta:
        model = ExpenseJun
        fields = "__all__"


class ExpenseFormJul(forms.ModelForm):
    class Meta:
        model = ExpenseJul
        fields = "__all__"


class ExpenseFormAug(forms.ModelForm):
    class Meta:
        model = ExpenseAug
        fields = "__all__"


class ExpenseFormSep(forms.ModelForm):
    class Meta:
        model = ExpenseSep
        fields = "__all__"


class ExpenseFormOct(forms.ModelForm):
    class Meta:
        model = ExpenseOct
        fields = "__all__"


class ExpenseFormNov(forms.ModelForm):
    class Meta:
        model = ExpenseNov
        fields = "__all__"


class ExpenseFormDec(forms.ModelForm):
    class Meta:
        model = ExpenseDec
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
