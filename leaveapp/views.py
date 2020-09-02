from django.shortcuts import render , redirect
from .forms import LeaveForm
from .models import Leave_data
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url="/accounts/login")
def leave_app(request):
    user = request.user
    if request.method == 'POST' :
        form = LeaveForm(request.POST)    
        if form.is_valid():

            leave_form = form.save(commit=False) 
            leave_form.user = user
            leave_form.save()
            return redirect('leave_app')
    else:
        form = LeaveForm()
        leaves_left = user.total_leaves_left
        return render(request, 'leave_app.html' , {'form' : form , 'leaves_left' : leaves_left})

@login_required(login_url="/accounts/login")
def approve(request):
    user = request.user
    if user.groups.filter(name='Manager').exists():
        leave_obj = Leave_data.objects.all()
        return render(request, 'approve.html' , {'leave_obj' : leave_obj})
    else:
        messages.error(request,'Login as Manager to access this page')
        return render(request, 'login.html')


@login_required(login_url="/accounts/login")
def approve_leave(request , id):
    user = request.user
    if user.groups.filter(name='Manager').exists():
        leave_obj = Leave_data.objects.get(id=id)
        leave_obj.is_approved = True
        leave_obj.save()
        return redirect('approve')
    else:
        messages.error(request,'Login as Manager to access this page')
        return render(request, 'login.html')

