from django.shortcuts import render,redirect

# Create your views here.


def ide(request):
    context = {}
    return render(request, 'ide/ide.html', context)

