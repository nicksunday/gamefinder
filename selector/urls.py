from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.GamesListView.as_view(), name='games'),
    path('search/', views.game_search_view, name='search'),
    path('selection/', views.game_selection_view, name='game_selection_view'),
    re_path(r'^game/(?P<pk>\d+)$', views.GamesDetailView.as_view(), name='games-detail'),
    path('visualization/', views.data_visualization_view, name='visualization'),
]
