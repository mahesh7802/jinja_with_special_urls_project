from django.urls import path
from app1.views import *
app_name='somthing'
urlpatterns=[
    path('function/',function,name='function'),
    path('money/',money,name='money'),
]