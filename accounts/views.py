from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_view(requests):
    if requests.user.is_authenticated:
        return render(requests, "accounts/already-logged-in.html", {})
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
    form = UserCreationForm(requests.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {'form': form}
    return render(requests, "accounts/register.html", context)


def already_logged_in(requests):
    return render(requests, "accounts/already-logged-in.html", {})
