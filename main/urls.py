from django.urls import path, include
from main.views import *
from . import views

#app_name = 'main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('news/', views.NewsList.as_view(), name = 'news'),
    path('authors/', views.AuthorsList.as_view(), name = 'authors'),
    path('dodaj_clanak', views.dodaj_clanak, name='dodaj_clanak'),
    path('izbrisi_clanak/<news_id>', views.izbrisi_clanak, name="delete-news"),
    path('azuriraj_autora/<author_id>', views.azuriraj_autor, name="update-author")
]
