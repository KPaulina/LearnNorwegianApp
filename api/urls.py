from django.urls import path
from .views import VocabularyDetailAPIView,VocabularyCreateAPIView


urlpatterns = [
    path('<int:pk>', VocabularyDetailAPIView.as_view()),
    path('', VocabularyCreateAPIView.as_view()),
]
