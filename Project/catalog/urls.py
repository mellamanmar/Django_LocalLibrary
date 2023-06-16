from django.urls import path
from .views import book, views
from .views import genre


urlpatterns= [
    path('', views.index, name= 'index')
]

urlpatterns+=[
    path ("genre", genre.GenreListView.as_view(), name= 'genre_list'),
]

urlpatterns +=[
    # path ('bookwild', book.book_list, name= 'book_wild'),
    path ('book', book.BookListView.as_view(), name= 'book_list'),
    path ('book/<int:pk>', book.BookDetailView.as_view(), name= 'book_detail'),
    
]