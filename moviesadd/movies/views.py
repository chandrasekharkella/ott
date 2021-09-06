
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def header(request):
    return render(request,'movies/header.html')
def index(request):
    telugu_movies = movies.objects.filter(status=1)
    img=main_banner.objects.all()
    tm=telugu_movies.filter(language='telugu')
    em=telugu_movies.filter(language='english')
    return render(request,'movies/index.html',{'tm': tm,'em':em,'img':img})

def catalog(request):
    return render(request,'movies/catalog.html')

def about(request):
    return render(request,'movies/about.html')

def cont(request):
    return render(request, 'movies/cont.html')



# def contacts(request):
#     return render(request, 'movies/contacts.html')


def details(request):
    telugu_movies = movies.objects.all()
    return render(request,'movies/details.html',{'tm': telugu_movies})

def telugu(request):
    telugu_movies = movies.objects.all().filter(status=1,language='telugu')
    return render(request, 'movies/telugu.html', {'tm': telugu_movies})

def english(request):
    telugu_movies = movies.objects.all()
    return  render(request,"movies/english.html",{'tm': telugu_movies})
def hindi(request):
    telugu_movies = movies.objects.all()
    return  render(request,"movies/hindi.html",{'tm': telugu_movies})



def signup(request):
    if request.method == 'POST':
        username=request.POST.get('regusername','')
        email=request.POST.get('regemail','')
        password=request.POST.get('regpassword','')
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('/')
    else:

        return render(request,'user/signup.html')
def signin(request):
    if request.method  == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User=authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
        return redirect('/')
    return render(request,'user/signin.html')
def logout_user(request):
    logout(request)
    return redirect('/')


def hero2(request):
    return render(request,'movies/heroslider2.html')


def reglog(request):
    return render(request,'user/reglog.html')




def add_movies(request):
    # if request.method == "POST":
    #     mv_form=movies_form(request.POST, request.FILES)
    #     if mv_form.is_valid():
    #         mv_form.save()
    # else:
    #     mv_form=movies_form()
    # return render(request,'dashboard/add_movies.html',{'mv_form':mv_form})

    #
    if request.method == "POST":
        mv_form = movies_form(request.POST, request.FILES)
        if mv_form.is_valid():
            mv_form.save()
    else:
        mv_form =movies_form()
    return render(request, 'dashboard/add_movies.html', {'mv_form': mv_form})


# ?publisher views
@login_required(login_url='/pub_login')

def publish(request):
    u=User.objects.all()

    list = movies.objects.all()
    list_paginator=Paginator(list,4)
    page_number=request.GET.get('page')
    page=list_paginator.get_page(page_number)
    context={
        'count':list_paginator.count,
        'page':page,
        'count1':u.count
    }
    return  render(request,'publisher/index.html',context)
def publist(request):
    return  render(request,'publisher/pub_list.html')
def pub_login(request):
    if request.method  == 'POST':
        username = request.POST.get('pubusername')
        password = request.POST.get('pubpassword')
        User=authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
        return redirect('/publish')
    return render(request,'user/publisherlogin.html')


# demoadd views
def update_status(request,status,id):
    movies.objects.filter(id=id).update(status=status)
    return redirect('/list')



