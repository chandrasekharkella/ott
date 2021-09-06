from django.urls import path
from dashboard import views

urlpatterns = [
    path('dash',views.dash,name='dash'),
    path('add',views.addmovie,name='add'),
    path('list',views.movies_list,name='list'),
    path('user',views.users,name='user'),
    path('comnt',views.comment,name='comnt'),
    path('reviews',views.reviews,name='reviews'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('add1',views.add_movies,name='add1'),
    path('padd',views.publisher_add,name='padd')



]