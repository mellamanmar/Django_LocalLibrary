from django.urls import path
from .views import book, views
from .views import genre
from .views import author
from .views import book_instance


urlpatterns= [
    path('', views.index, name= 'index'),
]

urlpatterns+=[
    path ("genre", genre.GenreListView.as_view(), name= 'genre_list'),
]

urlpatterns +=[
    path ('book', book.BookListView.as_view(), name= 'book_list'),
    path ('book/<int:pk>', book.BookDetailView.as_view(), name= 'book_detail'),
    path ('book/all', book.Book_allListView.as_view(), name='book_all')
]

urlpatterns +=[
    path ('author', author.AuthorListView.as_view(), name= 'author_list'),
    path ('author/<int:pk>', author.AuthorDetailView.as_view(), name= 'author_detail'),
]

urlpatterns+=[
    path ("instance/<int:pk>", book_instance.InstanceDetailView.as_view(), name= 'instance_detail'),
    path ("instance", book_instance.InstanceListView.as_view(), name= 'instance_list'),

]