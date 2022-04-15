from django.shortcuts import render
from .models import vocabulary
import random
from django import forms


class LearnNorwegianWords(forms.Form):
    user_input = forms.CharField(label="User input")


def index(request):

    return render(request, "norwegian/index.html", {"answers": request.session['answers']})


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


# answers = []


def create_list_of_words(request):
    '''
    Function that draws a random number and then checks if the user input is the same as the answer
    :param requests:
    :return:
    '''
    if 'answers' not in request.session:
        request.session['answers'] = []

    answers = request.session['answers']

    if "correct_answers" not in request.session:
        request.session["correct_answers"] = []

    correct_answers = request.session["correct_answers"]

    num = random.randint(0, 24)
    random_word = vocabulary.objects.all().values()[num]

    # answers.insert(0, random_word['word_in_norwegian'])
    request.session['answers'] += [random_word['word_in_norwegian']]

    if len(answers) >= 2:
        answer = answers[-2]
    else:
        answer = ''

    user_input = request.GET.get('user_input', 0)

    if answer == user_input:
        correct_answers.append(user_input)

    points = len(correct_answers)

    context = {'random_word': random_word, 'user_input': user_input, 'answer': answer,
               'correct_answers': correct_answers, 'points': points}
    return render(request, 'norwegian/train.html', context)
