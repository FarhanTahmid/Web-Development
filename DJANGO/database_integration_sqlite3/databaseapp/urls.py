from django.urls import path, include

from . import views

app_name= 'databaseapp'
urlpatterns = [
    #Include default auth urls
    path('', include('django.contrib.auth.urls')),
    #Registration page
    path('',views.showpage,name='signup'),
]