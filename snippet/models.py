from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from rest_framework import serializers



LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly',
                             max_length=100)

    class Meta:
        ordering = ('created',)

owner = models.ForeignKey('auth.User', related_name='myblog')

class myblog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    details= models.CharField(max_length=300)
    name=models.CharField(max_length=100)

def save(self, *args, **kwargs):

    super(Snippet, self).save(*args, **kwargs)

# I removed the previous code because it was not belonging to this models.py file from the scratch
#  I was meant to put that in serializers.py file and Now I'm doing this.
#  go to serializers.py and you will find out