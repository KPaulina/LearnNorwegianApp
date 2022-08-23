from django.test import TestCase
from .models import Vocabulary
# Create your test here.


class HomePageTestCase(TestCase):
    def setUp(self):
        Vocabulary.objects.create(id=200, word_in_norwegian='falle', word_in_english='fall', word_in_polish='spadać')
        Vocabulary.objects.create(id=201, word_in_norwegian='fare', word_in_english='throw', word_in_polish='rzucać')

    def test_vocabulary_adding_new_words(self):
        word = str(Vocabulary.objects.get(word_in_norwegian='fare'))
        self.assertEqual('fare rzucać', word)

    def test_vocabulary(self):
        list_of_wrods = Vocabulary.objects.all().values()
        self.assertEqual(2, len(list_of_wrods))
