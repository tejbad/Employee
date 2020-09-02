from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from django.conf import settings
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        emp_type = request.POST.get('emp_type')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email taken')
                return redirect('register')
            else:
                
                user = User.objects.create_user(username=email ,first_name=first_name, password=password1, email=email, last_name=last_name )
                user.save()
                if emp_type == "Manager":
                    my_group = Group.objects.get(name='Manager') 
                    my_group.user_set.add(user)
                elif emp_type == "Employee":
                    my_group = Group.objects.get(name='Employee') 
                    my_group.user_set.add(user)
                return redirect('login')
        else:
            messages.error(request,'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('leave_app')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url="/accounts/login")
def logout(request):
    auth.logout(request)
    return redirect('/')

