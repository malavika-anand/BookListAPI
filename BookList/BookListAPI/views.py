from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.

@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})

    elif request.method == 'POST':
        title=request.POST['title'],
        author=request.POST['author'],
        price=request.POST['price']
        inventory=request.POST.get('inventory', 1)
    
        book = Book(title=title, author=author, price=price, inventory=inventory)
        
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status = 400)
        
        return JsonResponse({'book': model_to_dict(book)}, status=201)