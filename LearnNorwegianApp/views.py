from django.shortcuts import render
from .models import vocabulary, uregelrette_verb
from random import sample
from django import forms
from django.views.generic import FormView, ListView
from .forms import SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

random_list = sample(range(25), 25)


class SearchingView(FormView):
    template_name = 'norwegian/search.html'
    form_class = SearchForm


class LearnNorwegianWords(forms.Form):
    user_input = forms.CharField(label="User input")


def index(request):
    return render(request, "norwegian/index.html", {})


def learn(request):
    return render(request, "norwegian/learn.html")


def vocab_to_learn(request):
    vocab_list = vocabulary.objects.all().select_related().order_by('id')
    context = {'data': vocab_list}
    return render(request, 'norwegian/words.html', context)


def verbs_to_learn(request):
    verb_list = vocabulary.objects.filter(category='verb')
    context = {'list_of_verbs': verb_list}
    return render(request, 'norwegian/verbs.html', context)


def train_vocabulary(request):
    '''
    Function that draws a random number in range to randomly choose a word in Polish and then checks if the user input is the same as the answer
    :param requests:
    :return:
    '''

    #TO DO: button that allows to do it once again

    if 'answers' not in request.session:
        request.session['answers'] = []

    answers = request.session['answers']

    if "correct_answers" not in request.session:
        request.session["correct_answers"] = []


    correct_answers = request.session["correct_answers"]

    if len(random_list) > 0:
        num = random_list[-1]
        random_word = vocabulary.objects.all().values()[num]
        request.session['answers'] += [random_word['word_in_norwegian']]
        random_list.pop(-1)
    else:
        random_word = 'Koniec zadania'

    if len(answers) >= 2:
        answer = answers[-2]
    else:
        answer = ''

    user_input = request.GET.get('user_input', 0)

    if answer == user_input:
        correct_answers.append(user_input)

    if random_word == 'Koniec zadania':
        end = 'Twój ostateczny wynik to:'
    else:
        end = ''

    points = len(correct_answers)

    context = {'random_word': random_word, 'user_input': user_input, 'answer': answer,
               'correct_answers': correct_answers, 'points': points, 'end': end}
    return render(request, 'norwegian/train.html', context)


def uregelrette_verbs(request):
    '''Showing Norwegian irregular verbs''' 
    irregular_verbs = uregelrette_verb.objects.all().select_related().order_by('id')
    context = {'irregular_verbs': irregular_verbs}
    return render(request, 'norwegian/irregular_verbs.html', context)


def search_words_view(request):
    query = request.GET.get('q')
    qs = vocabulary.objects.search(query=query)
    context = {
        'object_list': qs
    }
    return render(request, "norwegian/search.html", context)


class NorwegianListView(LoginRequiredMixin, ListView):
    model = vocabulary
    queryset = vocabulary.objects.all()
    context_object_name = 'words'


class NorwegianAddView(LoginRequiredMixin, CreateView):
    model = vocabulary
    fields = ['word_in_norwegian', 'word_in_polish', 'word_in_english', 'category']
