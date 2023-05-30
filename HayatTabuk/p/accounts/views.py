from collections import UserDict
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
#from django.contrib.auth.decorators import login_required
#from .forms import UpdateUserForm, UpdateProfileForm
#from django.contrib.auth import update_session_auth_hash
#from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


#creating the views for profile, login, logout, register
def profile(request):
        return render(request, 'accounts/profile.html')
#registeration function
def register(request):

    #statements for the registeration
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        #statement for the password if it's matchable
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'The following email does exist')
                return redirect(register)
            else:
                user = User.objects.create_user(first_name = first_name,last_name = last_name ,username = username,
            password = password, email = email)
                user.set_password(password)
                user.save()
                print("the registeration process is successfull! welcome")
                return redirect('login_user')
        else:
            messages.info(request, 'both passwords arent match, please enter again')
            return redirect(register)
    else:
        print("post method is not available")
        return render(request, 'accounts/register.html')
    
#log in function
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Username or password is invalid')
            return redirect('login_user')
        
    else:
        return render(request, 'accounts/login.html')

#logout function
def logout_user(request):
    auth.logout(request)
    return redirect('login_user')

'''''
#password reseting function
#references : https://stackoverflow.com/questions/1873806/how-to-allow-users-to-change-their-own-passwords-in-django
@login_required
def change_password(request):
   if request.method == 'POST':
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, UserDict)
            return redirect('company:Dashboard')
        else:
            return redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
        '''