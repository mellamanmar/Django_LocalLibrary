from typing import Any, Dict
from ..models.author import Author
# from ..models.book import Book
from django.views import generic
# from django.shortcuts import render
# from catalog.urls import pk


class AuthorListView(generic.ListView):
    model= Author
    context_object_name= 'author_list'
    template_name= 'author/author_list.html'

class AuthorDetailView (generic.DetailView):
    model= Author
    context_object_name= 'author_detail'
    template_name= 'author/author_detail.html'
    
# def list_authors (request):
#     books_list= Book.objects.filter(author__exact= "author_detail")
#     author_list= Author.objects.all()
#     return render(
#         request,
#         'author/author_list.html',
#         context={'books_list': books_list, 'author_list': author_list

#         }
#     )