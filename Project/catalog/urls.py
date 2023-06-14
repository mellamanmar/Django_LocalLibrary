from django.urls import path
from .views import views
from .views import genre, book


urlpatterns= [
    path('', views.index, name= 'index')
]

urlpatterns+=[
    path ("genre", genre.GenreListView.as_view(), name= 'genre_list'),
    path ("book", book.GenreListView.as_view(), name= 'book_list')

]