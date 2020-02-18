from django.shortcuts import render, redirect
from webapp.models import Expense
from webapp.form import ExpenseForm

# Create your views here.


def test(request):
    return render(request, "test.html")


def landing(request):
    return render(request, "landing.html")


def checkexpense(request):
    expense = Expense.objects.all()
    return render(request, "checkexpense.html", {'expense': expense})


def addexpense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/checkexpense")
    else:
        form = ExpenseForm()
        return render(request, "addexpense.html", {'form': form})


def options(request):
    return render(request, "options.html")
