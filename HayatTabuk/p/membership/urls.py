from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

urlpatterns = [

    path('membership', views.subscription, name='membership')
]
urlpatterns += staticfiles_urlpatterns()