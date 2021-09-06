
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from movies.forms import *

from movies.models import *
from.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here
def adminlogin(request):
    if request.method  == 'POST':
        username = request.POST.get('adminusername')
        password = request.POST.get('adminpassword')
        User=authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
        return redirect('/dash')
    return render(request,'user/adminlogin.html')

@login_required(login_url='/adminlogin')
def dash(request):
    if request.user.is_superuser:
        total_user=User.objects.all()
        total_movies=movies.objects.all()
        context ={
            'count':total_movies.count,
            'count1':total_user.count
        }
        return render(request, 'dashboard/index.html',context)
    else:
        return redirect('/')


def addmovie(request):
    return render(request,'dashboard/add-item.html')

def movies_list(request):
    u = User.objects.all()

    list = movies.objects.all()
    list_paginator = Paginator(list, 4)
    page_number = request.GET.get('page')
    page = list_paginator.get_page(page_number)
    context = {
        'count': list_paginator.count,
        'page': page,
        'count1': u.count
    }
    return render(request, 'dashboard/movies_list.html',context)


def users(request):
    return render(request,'dashboard/users.html')
def comment(request):
    return render(request,'dashboard/comments.html')

def reviews(request):
    return  render(request,'dashboard/reviews.html')


def add_movies(request):

    if request.method == "POST":
        mv_form = movies_form(request.POST, request.FILES)
        if mv_form.is_valid():
            mv_form.save()
    else:
        mv_form =movies_form()
    return render(request, 'dashboard/add_movies.html', {'mv_form': mv_form})

def publisher_add(request):

    if request.method == "POST":
        pb_form = publisher_form(request.POST, request.FILES)
        if pb_form.is_valid():
            pb_form.save()
            return redirect('/padd')
    else:
        pb_form =publisher_form()
    return render(request, 'dashboard/pub_add.html',{'pb_form': pb_form})


# ?crud operation views
def home(request):
    all_contact=contact.objects.all()
    return render(request,'home.html',{'all_contact':all_contact})