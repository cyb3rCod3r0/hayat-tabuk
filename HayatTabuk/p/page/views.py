from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'page/home.html')

def membership(request):
    return render(request, 'page/memberships.html')

def  personalTrainer(request):
    return render(request, 'page/personalTrainer.html')

def faq(request):
    return render(request, 'page/faq.html')

def classes(request):
    return render(request, 'page/class.html')

#def logIn(request):
 #   return render(request, 'page/register.html')

#def register(request):        
#    return render(request, 'page/register.html')
