from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.


def login_view(requests):
    if requests.method == "POST":
        form = AuthenticationForm(requests, data=requests.POST)
        if form.is_valid():
            user = form.get_user()
            login(requests, user)
            return redirect('/')
    else:
        form = AuthenticationForm(requests)
    context = {
        'form': form
    }
    return render(requests, "registration/login.html", context)


def logout_view(requests):
    if requests.method == 'POST':
        logout(requests)
        return redirect("/login/")
    return render(requests, "registration/logout.html", {})


def already_logged_in(requests):
    return render(requests, "registration/already-logged-in.html", {})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('LearnNorwegianApp:list')
    template_name = 'registration/register.html'


# class LoginView(CreateView):
#     form = AuthenticationForm
#     success_url = reverse_lazy('LearnNorwegianApp:list')
#     template_name = 'registration/login.html'
