from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),

    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('actor/', ActorViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='actor_list'),

    path('actor/<int:pk>/', ActorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='actor_detail'),

    path('director/', DirectorViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='director_list'),

    path('director/<int:pk>/', DirectorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='director_detail'),

    path('genre/', GenreViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='genre_list'),

    path('genre/<int:pk>/', GenreViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='genre_detail'),

    path('movie/', MovieViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='movie_list'),

    path('movie/<int:pk>/', MovieViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='movie_detail'),

    path('movieshots/', MovieShotsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='movieshots_list'),

    path('movieshots/<int:pk>/', MovieShotsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='movieshots_detail'),

    path('good/', GoodViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='good_list'),

    path('good/<int:pk>/', GoodViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='good_detail'),

    path('Comment/', CommentViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='comment_list'),

    path('comment/<int:pk>/', CommentViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment_detail'),

]
