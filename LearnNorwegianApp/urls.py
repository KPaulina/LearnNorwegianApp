"""LearnNorwegianApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import NorwegianListView, NorwegianAddView

app_name = 'LearnNorwegianApp'
urlpatterns = [
    path("", views.index, name="index"),
    path('learn', views.learn, name="learn"),
    path('words', views.vocab_to_learn, name="vocabulary"),
    path('verbs', views.verbs_to_learn, name="learning_verbs"),
    path('train', views.train_vocabulary, name="exercise"),
    path('irverbs', views.uregelrette_verbs, name='irr_verbs'),
    path('search', views.search_words_view, name='search-words'),
    #class based views
    path('list', NorwegianListView.as_view(), name='list'),
    path('add', NorwegianAddView.as_view(), name="add")
]

