from django.shortcuts import render

# Create your views here.

from ..models.author import Author
from ..models.genre import  Genre
from ..models.book import Book
from ..models.book_instance import BookInstance

def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()

    return render(
        request,
        'index.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors
        }
    )

