from django.shortcuts import render, redirect

# Create your views here.
def books(request):
    context = {}
    return render(request, 'books/read_books.html', context)