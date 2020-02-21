from django.shortcuts import render, redirect
from webapp.models import Expense, ExpenseJan, ExpenseFeb, ExpenseMar, ExpenseApr, ExpenseMay, ExpenseJun, ExpenseJul, ExpenseAug, ExpenseSep, ExpenseOct, ExpenseNov, ExpenseDec
from webapp.form import ExpenseForm, UserForm, RegForm, TestForm, ExpenseFormJan, ExpenseFormFeb, ExpenseFormMar, ExpenseFormApr, ExpenseFormMay, ExpenseFormJun, ExpenseFormJul, ExpenseFormAug, ExpenseFormSep, ExpenseFormOct, ExpenseFormNov, ExpenseFormDec
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
    return render(request, "checkexpense/checkexpense.html", {'expense': expense})


@login_required
def checkexpenseJan(request):
    expense = ExpenseJan.objects.all()
    return render(request, "checkexpense/checkexpenseJan.html", {'expense': expense})


@login_required
def checkexpenseFeb(request):
    expense = ExpenseFeb.objects.all()
    return render(request, "checkexpense/checkexpenseFeb.html", {'expense': expense})


@login_required
def checkexpenseMar(request):
    expense = ExpenseMar.objects.all()
    return render(request, "checkexpense/checkexpenseMar.html", {'expense': expense})


@login_required
def checkexpenseApr(request):
    expense = ExpenseApr.objects.all()
    return render(request, "checkexpense/checkexpenseApr.html", {'expense': expense})


@login_required
def checkexpenseMay(request):
    expense = ExpenseMay.objects.all()
    return render(request, "checkexpense/checkexpenseMay.html", {'expense': expense})


@login_required
def checkexpenseJun(request):
    expense = ExpenseJun.objects.all()
    return render(request, "checkexpense/checkexpenseJun.html", {'expense': expense})


@login_required
def checkexpenseJul(request):
    expense = ExpenseJul.objects.all()
    return render(request, "checkexpense/checkexpenseJul.html", {'expense': expense})


@login_required
def checkexpenseAug(request):
    expense = ExpenseAug.objects.all()
    return render(request, "checkexpense/checkexpenseAug.html", {'expense': expense})


@login_required
def checkexpenseSep(request):
    expense = ExpenseSep.objects.all()
    return render(request, "checkexpense/checkexpenseSep.html", {'expense': expense})


@login_required
def checkexpenseOct(request):
    expense = ExpenseOct.objects.all()
    return render(request, "checkexpense/checkexpenseOct.html", {'expense': expense})


@login_required
def checkexpenseNov(request):
    expense = ExpenseNov.objects.all()
    return render(request, "checkexpense/checkexpenseNov.html", {'expense': expense})


@login_required
def checkexpenseDec(request):
    expense = ExpenseDec.objects.all()
    return render(request, "checkexpense/checkexpenseDec.html", {'expense': expense})


@login_required
def addexpense(request):
    return render(request, "addexpense/addexpense.html")


@login_required
def addexpenseJan(request):
    if request.method == "POST":
        form = ExpenseFormJan(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseJan")
    else:
        form = ExpenseFormJan()
        return render(request, "addexpense/addexpenseJan.html", {'form': form})


@login_required
def addexpenseFeb(request):
    if request.method == "POST":
        form = ExpenseFormFeb(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseFeb")
    else:
        form = ExpenseFormFeb()
        return render(request, "addexpense/addexpenseFeb.html", {'form': form})


@login_required
def addexpenseMar(request):
    if request.method == "POST":
        form = ExpenseFormMar(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseMar")
    else:
        form = ExpenseFormMar()
        return render(request, "addexpense/addexpenseMar.html", {'form': form})


@login_required
def addexpenseApr(request):
    if request.method == "POST":
        form = ExpenseFormApr(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseApr")
    else:
        form = ExpenseFormApr()
        return render(request, "addexpense/addexpenseApr.html", {'form': form})


@login_required
def addexpenseMay(request):
    if request.method == "POST":
        form = ExpenseFormMay(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseMay")
    else:
        form = ExpenseFormMay()
        return render(request, "addexpense/addexpenseMay.html", {'form': form})


@login_required
def addexpenseJun(request):
    if request.method == "POST":
        form = ExpenseFormJun(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseJun")
    else:
        form = ExpenseFormJun()
        return render(request, "addexpense/addexpenseJun.html", {'form': form})


@login_required
def addexpenseJul(request):
    if request.method == "POST":
        form = ExpenseFormJul(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseJul")
    else:
        form = ExpenseFormJul()
        return render(request, "addexpense/addexpenseJul.html", {'form': form})


@login_required
def addexpenseAug(request):
    if request.method == "POST":
        form = ExpenseFormAug(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseAug")
    else:
        form = ExpenseFormAug()
        return render(request, "addexpense/addexpenseAug.html", {'form': form})


@login_required
def addexpenseSep(request):
    if request.method == "POST":
        form = ExpenseFormSep(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseSep")
    else:
        form = ExpenseFormSep()
        return render(request, "addexpense/addexpenseSep.html", {'form': form})


@login_required
def addexpenseOct(request):
    if request.method == "POST":
        form = ExpenseFormOct(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseOct")
    else:
        form = ExpenseFormOct()
        return render(request, "addexpense/addexpenseOct.html", {'form': form})


@login_required
def addexpenseNov(request):
    if request.method == "POST":
        form = ExpenseFormNov(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseNov")
    else:
        form = ExpenseFormNov()
        return render(request, "addexpense/addexpenseNov.html", {'form': form})


@login_required
def addexpenseDec(request):
    if request.method == "POST":
        form = ExpenseFormDec(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkexpense/checkexpenseDec")
    else:
        form = ExpenseFormDec()
        return render(request, "addexpense/addexpenseDec.html", {'form': form})


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
