from django.urls import path
from .views import VocabularyDetailAPIView


urlpatterns = [
    path('/<int:pk>', VocabularyDetailAPIView.as_view())
]
