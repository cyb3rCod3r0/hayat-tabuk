from django.shortcuts import render
from .models import Membership
# Create your views here.

def subscription(request):
    if request.method =="POST":
        membership = Membership()
        Fname=request.POST.get('Fname')
        Lname=request.POST.get('Lname')
        telephone=request.POST.get('telephone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        membership.Fname=Fname
        membership.Lname=Lname
        membership.telephone=telephone
        membership.subject=subject
        membership.message=message
        membership.save()
    return render(request, 'membership\memberships.html')
