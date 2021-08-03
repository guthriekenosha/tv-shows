from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index (request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request,'shows.html', context)

def add_show(request):
    return render(request, 'add_show.html')  

def create_show(request):
    print(request.POST['title'])
    errors = Show.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add_show')
    else:
        Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description']
        )
    return redirect('/shows')

def edit_show(request,id):
    details = Show.objects.get(id=id)
    context = {
        'shows': details 
    }
    return render(request, 'edit_show.html', context)

def all_shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request,'shows.html', context)

def new_show (request, id):
    details = Show.objects.get(id=id)
    context = {
        'show': details
    }
    return render(request, 'new_show.html', context)


def update(request,id):
    edit = Show.objects.get(id=id)
    edit.title = request.POST['title']
    edit.network = request.POST['network']
    edit.release_date = request.POST['release_date']
    edit.description = request.POST['description']
    edit.save()

    return redirect('/shows')

def delete(request, id):
    delete = Show.objects.get(id=id)
    delete.delete()
    return redirect('/shows')
