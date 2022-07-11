from django.test import TestCase
from .models import vocabulary
# Create your tests here.


class HomePageTestCase(TestCase):
    def setUp(self):
        vocabulary.objects.create(id=200, word_in_norwegian='falle', word_in_english='fall', word_in_polish='spadać')
        vocabulary.objects.create(id=201, word_in_norwegian='fare', word_in_english='throw', word_in_polish='rzucać')

    def test_vocabulary_adding_new_words(self):
        word = str(vocabulary.objects.get(word_in_norwegian='fare'))
        self.assertEqual('fare rzucać', word)

    def test_vocabulary(self):
        list_of_wrods = vocabulary.objects.all().values()
        self.assertEqual(2, len(list_of_wrods))
