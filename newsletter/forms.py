from django import forms
from .models import Subscriber

class SubscribeForm(forms.Form):
    email = forms.EmailField()
    class Meta:
        model = Subscriber
        fields = ['email']
