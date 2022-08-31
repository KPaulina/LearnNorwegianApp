from rest_framework import serializers
from LearnNorwegianApp.models import Vocabulary


class VocabularySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='vocabulary-edit',
                                               lookup_field='pk')
    class Meta:
        model = Vocabulary
        fields = [
            'url',
            'word_in_norwegian',
            'word_in_polish',
            'word_in_english',
            'category',
        ]
