from django.urls import path
from .import views
urlpatterns = [

    path('',views.userRegistration,name='register'),
    path('register',views.userRegistration,name='register'),
    path('homepage',views.homepage,name='homepage')
]