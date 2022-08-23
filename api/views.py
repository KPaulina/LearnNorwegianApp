
from LearnNorwegianApp.models import Vocabulary
from rest_framework import generics
from .serializers import VocabularySerializer
# Create your views here.


class VocabularyDetailAPIView(generics.RetrieveAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer

