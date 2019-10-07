from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm,UserUpdateForm,ProfileForm

def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        new_obj = form.save(commit=False)
        new_obj.set_password(form.cleaned_data.get('password2'))
        new_obj.save()
        messages.success(request,"You are successfully registered.Now you can Login!")
        return redirect('/')
    return render(request,'accounts/register.html',{'form':form,'section':'register'})

@login_required
def dashboard(request):
    return render(request,'accounts/dashboard.html',{'section':'dashboard'})

@login_required
def edit_profile(request):
    u_form = UserUpdateForm(request.POST or None,instance=request.user)
    p_form = ProfileForm(request.POST or None,request.FILES or None,instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request,"Profile Updated!!!")
        return redirect('dashboard')
    return render(request,'accounts/profile_form.html',{'section':'dashboard','u_form':u_form,'p_form':p_form})
