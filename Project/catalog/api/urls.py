from django.urls import path
from catalog.api.views.author import AuthorView


urlpatterns = [
    path ('author', AuthorView.as_view(), name= 'authors_list'),
    path ('author/<int:id>', AuthorView.as_view(), name= 'authors_id')
]
