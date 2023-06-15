from ..models.book import Book
from ..models.book_instance import BookInstance
from django.shortcuts import render
from django.views import generic


def book_list(request):
    wild_books= Book.objects.filter(title__contains='wild').all()

    return render(
        request,
        'book/book_wild.html',
        context= {'wild_books': wild_books }
    )

class BookListView(generic.ListView):
    model= Book
    context_object_name= 'book_list1'
    template_name= 'book/book_detail.html'


class BookDetailView(generic.DetailView):
    model= Book
    context_object_name= 'book_detail'
    template_name = "book/book_detail.html"
    # def get_queryset(self):
    #     book_detail= Book.objects.all()
    #     return book_detail

class StatusListView(generic.ListView):
    model= BookInstance
    context_object_name= 'book_status'
    template_name= "book/book_detail.html"