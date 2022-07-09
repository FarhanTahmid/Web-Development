from django.urls import path
from .import views
urlpatterns = [

    path('',views.userRegistration,name='register'),
    path('register',views.userRegistration,name='register'),
    path('homepage',views.homepage,name='homepage'),
    path('logged_in',views.logged_in,name='logged_in'),
    path('logout',views.logout,name='logout')
]