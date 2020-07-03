# chat/views.py
from django.shortcuts import render,redirect
from .models import user_bot,Message

from threading import *

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })



