from django.shortcuts import render
from .models import vocabulary
import random
from django import forms


class LearnNorwegianWords(forms.Form):
    user_input = forms.CharField(label="User input")


def index(request):
    return render(request, "norwegian/index.html")


def learn(request):
    # if request.method == "POST":
    #     form = LearnNorwegianWords(request.POST)
    #     if form.is_valid():
    #         word = form.cleaned_data["user_input"]
    #         list_of_words.append(word)
    #     else:
    #         return render(request, "norwegian/learn.html", {"form": form})
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


answers = []


def create_list_of_words(requests):
    '''
    Function that draws a random number and then checks if the user input is the same as the answer
    :param requests:
    :return:
    '''

    num = random.randint(0, 24)
    random_word = vocabulary.objects.all().values()[num]

    answers.insert(0, random_word['word_in_norwegian'])
    if len(answers) >= 2:
        answer = answers[1]
    else:
        answer = ''

    user_input = requests.GET.get('user_input', 0)

    context = {'random_word': random_word, 'user_input': user_input, 'answer': answer}
    return render(requests, 'norwegian/train.html', context)
