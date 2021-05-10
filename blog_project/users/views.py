from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    uerror = ""
    werror = ""
    if request.method=='POST':
        u_form = UserRegisterForm(request.POST)
        w_form = WorkingRegisterForm(request.POST, request.FILES)
        if u_form.is_valid() and w_form.is_valid():
            user = u_form.save()
            uname = u_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {uname}!')
            wuser = w_form.save(commit=False)
            wuser.user=user
            wuser.type="WorkingUser"
            wuser.save()
            return redirect('login')
        else:
            uerror = u_form.errors
            werror = w_form.errors
    else:
        u_form = UserRegisterForm()
        w_form = WorkingRegisterForm()
    return render(request,'users/signup.html',{'u_form':u_form,'w_form':w_form,'uerror':uerror,'werror':werror})


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_uform = UserUpdateForm(request.POST,instance = request.user)
        w_uform = WorkingUpdateForm(request.POST, request.FILES, instance=request.user.working_user)
        if u_uform.is_valid() and w_uform.is_valid():
            u_uform.save()
            w_uform.save()
            messages.success(request, f'profile updated !')
            return redirect('update_profile')
        else:
            uerror = u_uform.errors
            werror = w_uform.errors
    else:
        u_uform = UserUpdateForm(instance = request.user)
        w_uform = WorkingUpdateForm(instance = request.user.working_user)
    return render(request,'users/profile.html',{'u_uform':u_uform,'w_uform':w_uform})
