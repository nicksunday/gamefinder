from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.GamesListView.as_view(), name='games'),
    path('search/', views.game_selection_view, name='search'),
    re_path(r'^game/(?P<pk>\d+)$', views.GamesDetailView.as_view(), name='games-detail'),
]
