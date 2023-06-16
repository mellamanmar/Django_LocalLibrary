from ..models.book import Book
from ..models.book_instance import BookInstance
from django.shortcuts import render
from django.views import generic


class BookListView(generic.ListView):
    model = Book
    paginate_by = 5
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='wild')[:5] # Get 5 books containing the title war
    template_name = 'book/book_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model= Book
    paginate_by = 5
    context_object_name= 'book_detail'
    template_name = "book/book_detail.html"

class Book_allListView(generic.ListView):
    model = Book
    paginate_by = 5
    context_object_name = 'all_book'   # your own name for the list as a template variable
    template_name = 'book/all_book.html'  # Specify your own template name/locati