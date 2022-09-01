from LearnNorwegianApp.models import Vocabulary
from rest_framework import serializers


def validate_word_in_norwegian(value):
    qs = Vocabulary.objects.filter(word_in_norwegian__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f'{value} already exists')
    return value
