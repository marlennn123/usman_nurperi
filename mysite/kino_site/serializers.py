from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'all'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = 'all'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'all'


class GenreSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'all'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'all'


class MovieShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShots
        fields = 'all'


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = 'all'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'all'
