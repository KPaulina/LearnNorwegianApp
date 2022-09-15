from django.test import TestCase
from .models import Vocabulary
from django.test import Client
# Create your test here.


class HomePageTestCase(TestCase):
    def setUp(self):
        Vocabulary.objects.create(id=200, word_in_norwegian='falle', word_in_english='fall', word_in_polish='spadać')
        Vocabulary.objects.create(id=201, word_in_norwegian='fare', word_in_english='throw', word_in_polish='rzucać')

    def test_vocabulary_adding_new_words(self):
        word1_id = Vocabulary.objects.get(word_in_norwegian='fare').id
        word2_id = Vocabulary.objects.get(word_in_polish='rzucać').id
        self.assertEqual(word1_id, word2_id)

    def test_vocabulary(self):
        list_of_wrods = Vocabulary.objects.all().values()
        self.assertEqual(2, len(list_of_wrods))

    def test_words_id(self):
        word1_id = Vocabulary.objects.get(word_in_norwegian='falle').id
        word2_id = Vocabulary.objects.get(word_in_polish='rzucać').id
        self.assertNotEqual(word1_id, word2_id)

    def test_page_with_words(self):
        c = Client()
        response = c.get('/vocab/words')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['data'].count(), 2)



