from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_view(requests):
    if requests.user.is_authenticated:
        return render(requests, "account/already-logged-in.html", {})
    if requests == "POST":
        username = requests.POST.get("username")
        password = requests.POST.get("passowrd")
        user = authenticate(username=username, password=password)
        if user is None:
            context = {'error': 'Niepoprawne hasło lub login'}
            return render(requests, "accounts/login.html", context)
        login(requests, user)
        return redirect('/')
    return render(requests, "accounts/login.html", {})


def logout_view(requests):
    if requests.method == 'POST':
        logout(requests)
        return redirect("/login/")
    return render(requests, "accounts/logout.html", {})


def register_view(requests):
    return render(requests, "accounts/register.html", {})
