from django.shortcuts import render
from .forms import StudentForm

# Create your views here.

def homepage(r):
    return render(r,'index.html')

def applyForAdmission(r):
    form = StudentForm(r.POST or None, r.FILES or None)

    return render(r,'apply.html', {'form':form})

def login(r):
    return render(r, 'login.html')