from multiprocessing import context
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1,'name':'Lets learn python!'},
    {'id': 2,'name':'Discord Club'},
    {'id': 3,'name':'Lets learn JS!'},
    {'id': 4,'name':'Lets learn DSA!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')