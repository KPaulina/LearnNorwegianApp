from rest_framework import serializers

from LearnNorwegianApp.models import Vocabulary


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = [
            'word_in_norwegian',
            'word_in_polish',
            'word_in_english',
            'category',
        ]
