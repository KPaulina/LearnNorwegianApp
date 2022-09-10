from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Vocabulary


@register(Vocabulary)
class VocabularyIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'word_in_norwegian',
        'word_in_polish',
        'word_in_english',
        'category',
    ]
