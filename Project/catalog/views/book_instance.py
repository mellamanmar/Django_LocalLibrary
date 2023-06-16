from django.views import generic
from ..models.book_instance import BookInstance


class InstanceListView(generic.ListView):
    model= BookInstance
    context_object_name= 'instance_list'
    template_name= 'book_instance/instance_list.html'

class InstanceDetailView (generic.DetailView):
    model= BookInstance
    context_object_name= 'instance_detail'
    template_name= 'book_instance/instance_detail.html'