from django.urls import path
from . import views


urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('exists', views.already_logged_in, name="already-logged-in"),
    path('register', views.register_view, name="register")
]
