from django.urls import path
from .views import *



urlpatterns = [    
    path('padre/', padre),
    path('madre/', madre),
    path('primo/', primo),
    path('', inicio),

]