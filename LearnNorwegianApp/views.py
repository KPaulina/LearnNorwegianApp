from django.shortcuts import render
from django.http import HttpResponse
from .models import vocabulary
import random
from django.forms.models import model_to_dict


def index(request):
    return render(request, "norwegian/index.html")


def learn(request):
    return render(request, "norwegian/learn.html")


def vocab_to_learn(request):
    vocab_list = vocabulary.objects.all().select_related().order_by('id')
    # vocab_list = vocabulary.objects.raw('SELECT * FROM public."LearnNorwegianApp_vocabulary"')
    context = {'data': vocab_list}
    return render(request, 'norwegian/words.html', context)


def verbs_to_learn(request):
    verb_list = vocabulary.objects.filter(category='verb')
    context = {'list_of_verbs': verb_list}
    return render(request, 'norwegian/verbs.html', context)


def create_list_of_words(requests):
    # list_of_dicts = [{i.word_in_norwegian: i.word_in_polish} for i in vocabulary.objects.all()]
    num = random.randint(0, 24)
    random_word = vocabulary.objects.all().values()[num]
    print(random_word)
    context = {'random_word': random_word}
    return render(requests, 'norwegian/train.html', context)
