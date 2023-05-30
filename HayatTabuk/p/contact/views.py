from django.shortcuts import render
from .models import Conact
from pdb import post_mortem
#Create your views here.

#function for contact page
def contact(request):

    if request.method == "POST":
        contact = Conact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

    return render(request, 'contact/contact.html',{'post':post_mortem})
