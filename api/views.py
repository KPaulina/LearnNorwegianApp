from LearnNorwegianApp.models import Vocabulary
from rest_framework import generics
from .serializers import VocabularySerializer
# Create your views here.


class VocabularyDetailAPIView(generics.RetrieveAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer


class VocabularyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer


class VocabularyDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer
    lookup_field = 'pk'

