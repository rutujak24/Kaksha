from django.shortcuts import render,redirect, HttpResponse
from .forms import SubscribeForm
from .models import Subscriber
from django.core.mail import send_mail
#from django.contrib import messages

# Create your views here.

def subscribe(request):
    if request.method == 'POST':
        my_mail=request.POST.get('email')
        s = Subscriber(email=my_mail)
        if not Subscriber.objects.filter(email=my_mail).exists():
            s.save()
            send_mail('Kaksha: Subscription Successful!','Hi there! \n\nThis email confirms your subscription for Kaksha Newsletter. Thanks for choosing us! \n\nRegards, \nRutuja from Kaksha!','rutuuuujaaaa@gmail.com',[my_mail],fail_silently=False)
        else:
            send_mail('Kaksha: Already Subscribed!','Hi there! \n\nThis email confirms that you are already subscribed for Kaksha Newsletter. Thanks for choosing us! \n\nRegards, \nRutuja from Kaksha!','rutuuuujaaaa@gmail.com',[my_mail],fail_silently=False)
        return redirect('landing-page')
    return redirect('landing-page')
