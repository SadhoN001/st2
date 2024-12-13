from django.urls import path
from . import views



urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('portfol/', views.portfol, name='portfol'),
    path('about-us/', views.about_us, name='about-us'),
    path('userform/', views.userform, name='userform'),
    path('submitform/', views.submitform, name='submitform'),
    path('calculator/', views.calculator, name='calculator'),
    path('evanodd/', views.evanodd, name='evanodd'),
    path('todos/', views.todos, name='todos'),
    
]