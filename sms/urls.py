
from django.contrib import admin
from django.urls import path

from schoolwork.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name='homepage'),
    path('apply/',applyForAdmission, name='apply'),
    path('login/',login, name='login')
]
