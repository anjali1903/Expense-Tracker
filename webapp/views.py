from django.shortcuts import render, redirect
from webapp.models import Expense, ExpenseJan, ExpenseFeb
from webapp.form import ExpenseForm, UserForm, RegForm, TestForm, ExpenseFormJan, ExpenseFormFeb
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def test(request):
    return render(request, "test.html")


def landing(request):
    return render(request, "landing.html")


@login_required
def checkexpense(request):
    expense = Expense.objects.all()
    username = request.user.username
    return render(request, "checkexpense.html", {'expense': expense, 'username': username})


@login_required
def checkexpenseJan(request):
    expense = ExpenseJan.objects.all()
    return render(request, "checkexpenseJan.html", {'expense': expense})


@login_required
def checkexpenseFeb(request):
    expense = ExpenseFeb.objects.all()
    return render(request, "checkexpenseFeb.html", {'expense': expense})


@login_required
def addexpense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/checkexpense")
    else:
        form = ExpenseForm()
        return render(request, "addexpense.html", {'form': form})


@login_required
def addexpenseJan(request):
    if request.method == "POST":
        form = ExpenseFormJan(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/checkexpenseJan")
    else:
        form = ExpenseFormJan()
        return render(request, "addexpenseJan.html", {'form': form})


@login_required
def addexpenseFeb(request):
    if request.method == "POST":
        form = ExpenseFormFeb(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/checkexpenseFeb")
    else:
        form = ExpenseFormFeb()
        return render(request, "addexpenseFeb.html", {'form': form})


@login_required
def delete(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect("/checkexpense")


# def options(request):
 #   return render(request, "options.html")


def customreg(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        form = RegForm(request.POST)
        if user.is_valid() and form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            user.save()
            profile.save()
            return redirect("/login/")
    else:
        user = UserForm()
        form = RegForm()
    return render(request, "registration/customreg.html", {'form': form, 'user': user})


def check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)  # logs in the user
        return redirect("/options")
    else:
        return redirect("/login")


@login_required
def options(request):
    username = request.user.username
    return render(request, "options.html", {'username': username})


def logoutview(request):
    logout(request)  # logsout the current user
    return redirect("/landing")
