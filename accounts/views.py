from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

# Create your views here.


def login_view(requests):
    if requests == "POST":
        form = AuthenticationForm(requests, data=requests.POST)
        if form.is_valid():
            user = form.get_user()
            login(requests, user)
            return redirect('/')
    else:
        form = AuthenticationForm(requests)
    context = {'form': form}
    return render(requests, "accounts/login.html", context)


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
