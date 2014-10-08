__author__ = 'mj'

from django.forms import widgets
from rest_framework import serializers
from snippet.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from snippet.models import myblog
from django.contrib.auth.models import User

# Version 1 of SnippetSerializers
# This is old tech code.
# class SnippetSerializer(serializers.Serializer):
#     pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
#     title = serializers.CharField(required=False,
#                                   max_length=100)
#     code = serializers.CharField(widget=widgets.Textarea,
#                                  max_length=100000)
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
#                                        default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES,
#                                     default='friendly')
#
#     def restore_object(self, attrs, instance=None):
#         """
#         Create or update a new snippet instance, given a dictionary
#         of deserialized field values.
#
#         Note that if we don't define this method, then deserializing
#         data will simply return a dictionary of items.
#         """
#         if instance:
#             # Update existing instance
#             instance.title = attrs.get('title', instance.title)
#             instance.code = attrs.get('code', instance.code)
#             instance.linenos = attrs.get('linenos', instance.linenos)
#             instance.language = attrs.get('language', instance.language)
#             instance.style = attrs.get('style', instance.style)
#             return instance
#
#         # Create new instance
#         return Snippet(**attrs)

# Snippet serializer works the same as the above class
# This will work with model serializers directly and convert all data to serializers


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = myblog
        fields = ('id','name','title','details')

class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(many=True)
    owner = serializers.Field(source='owner.username')
    class Meta:
        model = User
        owner = User
        fields = ('id', 'username', 'blogs')
