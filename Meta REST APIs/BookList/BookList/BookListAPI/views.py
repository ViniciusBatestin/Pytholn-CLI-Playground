from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse, Http404
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books' : list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        inventory = request.POST.get('iventory')

        book = Book(title=title, author=author, price=price, inventory=inventory)

        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true', 'message': 'required field missing'}, status=400)
    return JsonResponse(model_to_dict(books), status = 201)


@require_http_methods(['GET'])
def book(request, pk):
    try:
        _book = Book.objects.get(pk=pk)
        return JsonResponse(model_to_dict(_book))
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
