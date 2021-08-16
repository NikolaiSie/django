from django.shortcuts import render
import numpy as np
import datetime

from .models import Haiku, Chapter, Poem

def index(request):
    haiku_id = datetime.datetime.now().strftime("%d")
    # Temp solution
    haiku_id = 1
    haiku = Haiku.objects.get(pk=haiku_id)
    return render(request, 'home.html', {'haiku':haiku, "line": haiku_id})


def haiku_by_id(request, haiku_id):
    haiku = Haiku.objects.get(pk=haiku_id)
    return render(request, 'haiku.html', {'haiku':haiku})

def odinsbane(request):
    prologue = Chapter.objects.get(pk=1)
    chapter1 = Chapter.objects.get(pk=2)
    return render(request, 'odinsbane.html', {'prologue':prologue, 'chapter1':chapter1})

def poem(request):
    poem = Poem.objects.get(pk=np.random.randint(1,2))
    return render(request, 'poem.html', {'poem':poem})


def author(request):
    return render(request, 'author.html')