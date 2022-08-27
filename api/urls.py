from django.urls import path
from .views import VocabularyDetailAPIView, VocabularyListCreateAPIView, \
    VocabularyDeleteUpdateAPIView


urlpatterns = [
    path('<int:pk>', VocabularyDetailAPIView.as_view()),
    path('<int:pk>/edit', VocabularyDeleteUpdateAPIView.as_view()),
    path('', VocabularyListCreateAPIView.as_view()),
]
