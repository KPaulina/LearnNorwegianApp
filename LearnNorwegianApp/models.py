from django.db import models


class vocabulary(models.Model):
    id = models.IntegerField(primary_key=True)
    word_in_norwegian = models.CharField(max_length=70)
    word_in_polish = models.CharField(max_length=70)
    word_in_english = models.CharField(max_length=70, blank=True)
    category = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return self.word_in_norwegian + " " + self.word_in_polish


class uregelrette_verb(models.Model):
    id = models.IntegerField(primary_key=True)
    infinitiv = models.CharField(max_length=50)
    presens = models.CharField(max_length=50)
    preteritum = models.CharField(max_length=50)
    presens_perfektum = models.CharField(max_length=50)
    polski = models.CharField(max_length=50)

    def __str__(self):
        return self.infinitiv + ' ' + self.polski
