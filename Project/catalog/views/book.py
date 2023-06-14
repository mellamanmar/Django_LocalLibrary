from django.views import generic
from ..models.book import Book

class GenreListView (generic.ListView):
    model= Book
    context_object_name= 'book_list'
    template_name= 'book/book_list.html'