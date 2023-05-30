from django.urls import path
from app2.views import *
app_name='nothing'
urlpatterns=[
    path('parents/',parents,name='parents'),
    path('jinjaindex/',jinjaindex,name='jinjaindex'),
]