from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
#    path('memberships', views.membership, name = 'memberships'),
    path('personalTrainer', views.personalTrainer, name = 'personalTrainer'),
#    path('logIn', views.logIn, name = 'Log in'),
#    path('register', views.register, name = 'sign up'),
    path('faq', views.faq, name = 'faq'),
    path('class', views.classes, name = 'class')

]