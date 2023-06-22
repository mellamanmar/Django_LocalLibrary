from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import *
from catalog.models.author import Author
import json

class AuthorView (View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id= 0):
        if (id> 0):
            authors= list(Author.objects.filter(id=id).values())
            if len(authors) > 0:
                author = authors [0]
                datos= {'message': "Success", 'author': author}
            else:
                datos= {'message': "Author not found"}
            return JsonResponse (datos)
        authors= list(Author.objects.values())
        if len(authors)> 0:
            datos= {'message': "Success", 'authors': authors}
        else:
            datos= {'message': "Author not found"}
        return JsonResponse(datos)
  
    def post(self, request):
        jd= json.loads(request.body)
        # print (jd)
        # print(request.body)
        new_author= Author.objects.create(first_name= jd['first_name'], last_name= jd["last_name"], date_of_birth= jd["date_of_birth"])
        new_author= {'message': "Success"}
        return JsonResponse (new_author)

    def put(self, request, id):
        jd= json.loads(request.body)
        authors= list(Author.objects.filter(id=id).values())
        if len(authors) > 0:
            author= Author.objects.get(id=id)
            author.first_name= jd['first_name']
            author.last_name= jd["last_name"]
            author.date_of_birth= jd['date_of_birth']  
            author.save()
            datos= {'message': "Success"}
        else:
            datos= {'message': "Author not found"}
        return JsonResponse (datos)

    def delete(self, request, id):
        authors= list(Author.objects.filter(id=id).values())
        if len(authors) > 0:
            Author.objects.filter(id=id).delete()
            datos= {'message': "Success"}
        else:
            datos= {'message': "Author not found"}
        return JsonResponse (datos)
