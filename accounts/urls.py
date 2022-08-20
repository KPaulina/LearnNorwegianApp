from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('exists', views.already_logged_in, name="already-logged-in"),
    path('signup', SignUpView.as_view(), name='signup'),
]
