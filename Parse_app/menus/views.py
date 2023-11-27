from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import AccountForm
# Create your views here.

def homepage(request):
    template = loader.get_template('Homepage.html')
    return HttpResponse(template.render())

def createAccount(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        form.save()
        return redirect('')
    else:
        form = AccountForm()
    return render(request,
                  'Account_Creation.html',
                  {"form": form})

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def courses(request):
    template = loader.get_template('Courses.html')
    return HttpResponse(template.render())
