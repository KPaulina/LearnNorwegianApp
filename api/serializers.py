from rest_framework import serializers
from LearnNorwegianApp.models import Vocabulary
from .validators import validate_word_in_norwegian


class VocabularySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='vocabulary-edit',
                                               lookup_field='pk')
    word_in_norwegian = serializers.CharField(validators=[validate_word_in_norwegian])
    class Meta:
        model = Vocabulary
        fields = [
            'url',
            'word_in_norwegian',
            'word_in_polish',
            'word_in_english',
            'category',
        ]


