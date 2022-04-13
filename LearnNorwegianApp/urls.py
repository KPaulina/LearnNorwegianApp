from django.urls import path
from . import views
from .views import vocab_to_learn

urlpatterns = [
    path("", views.index, name="index"),
    path('learn', views.learn, name="learn"),
    path('words', views.vocab_to_learn, name="vocabulary"),
    path('verbs', views.verbs_to_learn, name="vocabulary"),
    path('train', views.create_list_of_words, name="vocabulary")
]
