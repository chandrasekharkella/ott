from django.contrib import admin
from django.urls import path
from movies import views
from django.core.paginator import Paginator

urlpatterns = [
    path('', views.index),

    path('catalog', views.catalog, name='catalog'),
    path('about', views.about, name='about'),
    path('cont', views.cont, name='cont'),
    # path('contacts', views.contacts, name='contacts'),

    path('details', views.details, name='details'),
    path('telugu', views.telugu, name='telugu'),
    path('english', views.english, name='english'),

    path('hindi', views.hindi, name='hindi'),

    path('header',views.header),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('logout_user',views.logout_user,name='logout_user'),

    path('hero/',views.hero2,name='hero'),
    path('reglog/',views.reglog,name='reglog'),
    path('update_status/<int:status>/<int:id>',views.update_status,name='update_status'),



# ?dashboard urls

    # path('dash',views.dash,name='dash'),
    # path('add',views.addmovie,name='add'),
    # path('list',views.movies_list,name='list'),
    # path('user',views.users,name='user'),
    # path('comnt',views.comment,name='comnt'),
    # path('reviews',views.reviews,name='reviews'),
    # path('adminlogin',views.adminlogin,name='adminlogin'),
    # path('add1',views.add_movies,name='add1'),
    #



# publisher urls

    path('publish',views.publish,name="publish"),
    path('publist',views.publist,name="publist"),
    path('pub_login',views.pub_login,name='pub_login'),


]
