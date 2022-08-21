from django.shortcuts import render
from django.http import JsonResponse
from LearnNorwegianApp.models import vocabulary
# Create your views here.


def api_home(request, *args, **kwargs):
    model_data = vocabulary.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['word_in_norwegian'] = model_data.word_in_norwegian
        data['word_in_english'] = model_data.word_in_english
        data['word_in_polish'] = model_data.word_in_polish
        data['category'] = model_data.category
    return JsonResponse(data)
