from ..models.book import Book
from ..models.language import Language
from django.shortcuts import render
from django.views import generic


# def book_list(request):
#     wild_books= Book.objects.filter(title__contains='wild').all()

#     return render(
#         request,
#         'book/book_wild.html',
#         context= {'wild_books': wild_books }
    # )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 5
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='wild')[:5] # Get 5 books containing the title war
    template_name = 'book/book_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model= Book, Language
    paginate_by = 5
    context_object_name= 'book_detail'
    template_name = "book/book_detail.html"

# def book_detail (request, pk):
#     detail= Book.objects.all()
#     language_book= Language.objects.all()
#     return render (request, 'book/book_detail.html', context= {'detail': detail, 'language_book': language_book})
    

# class StatusListView(generic.ListView):
#     model= BookInstance
#     context_object_name= 'book_status'
#     template_name= "book/book_detail.html"