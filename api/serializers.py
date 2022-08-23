from rest_framework import serializers

from LearnNorwegianApp.models import vocabulary


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = vocabulary
        fields = [
            'word_in_norwegian',
            'word_in_polish',
            'word_in_english',
            'category',
        ]
