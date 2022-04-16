
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('aboutus',views.about,name='about'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    # path('base',views.base,name='base')
]
