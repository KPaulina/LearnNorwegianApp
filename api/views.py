from django.shortcuts import render
from django.http import JsonResponse
from LearnNorwegianApp.models import vocabulary
from rest_framework.decorators import api_view
from .serializers import VocabularySerializer
# Create your views here.


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = vocabulary.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = VocabularySerializer(instance).data
    return JsonResponse(data)
