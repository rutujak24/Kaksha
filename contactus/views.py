from django.shortcuts import render,redirect,HttpResponse
from .forms import ContactUsForm
from django.core.mail import send_mail
from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            my_mail=request.POST.get('email')
            my_name =request.POST.get('name')
            subject =request.POST.get('subject')
            message =request.POST.get('message')

            send_mail('Kaksha: Get in Touch!','Hello Rutuja! \n\nRecently someone has reached out to us. Here are the senders details. \nName: '+str(my_name)+ '\nEmail: '
            +str(my_mail)+ '\nSubject: '+str(subject)+ '\nMessage: '+str(message)+'\n\nFrom Kaksha Website!','rutuuuujaaaa@gmail.com',['rutuuuujaaaa@gmail.com'],fail_silently=False,)

            send_mail('Kaksha: Message Recieved!','Hello! \n\nThis is to confirm that, we have recieved your message. Soon we will get in touch with you. \n\nAutomated mail from Kaksha!','rutuuuujaaaa@gmail.com',[my_mail],fail_silently=False,)
   
            return HttpResponse(content="Your message is sent. Thank you!",status=201)
    return HttpResponse(content="<p>Error sending message</p>")
    