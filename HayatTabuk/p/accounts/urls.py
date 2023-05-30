from django.urls import path
from django.contrib.auth import views as auth_views
from .views import profile, register, logout_user, login_user

urlpatterns = [
    path('profile.html', profile, name = 'profile'), #directory for profile and it has updating the user's data
    path('register.html', register, name = 'register'), #directory for registeration page
    path('login_user', login_user, name = 'login_user' ), #directory for login page
    path('logout_user', logout_user, name = 'logout_user'), #directory for logout to the login
    #path('change_password', change_password, name = 'change_password'), #direcoty for changing password page
]