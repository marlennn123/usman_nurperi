from rest_framework import viewsets,  permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import MovieFilter
from rest_framework.pagination import PageNumberPagination


class MovieAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 1000

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ActorViewSets(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DirectorViewSets(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenreViewSets(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MovieViewSets(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = MovieFilter
    filterset_class = MovieFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MovieShotsViewSets(viewsets.ModelViewSet):
    queryset = MovieShots.objects.all()
    serializer_class = MovieShotsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
