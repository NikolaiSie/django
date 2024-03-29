from django.shortcuts import render
import numpy as np
import datetime

from .models import Haiku, Chapter, Poem, Story

def index(request):
    haiku_id = datetime.datetime.now().strftime("%d")
    haiku = Haiku.objects.get(pk=haiku_id)
    haiku_id = haiku_id.lstrip("0")
    return render(request, 'home.html', {'haiku': haiku, "line": haiku_id})


def haiku_by_id(request, haiku_id):
    haiku = Haiku.objects.get(pk=haiku_id)
    return render(request, 'haiku.html', {'haiku': haiku})

def odinsbane(request):
    prologue = Chapter.objects.get(pk=1)
    chapter1 = Chapter.objects.get(pk=2)
    chapter2 = Chapter.objects.get(pk=3)
    return render(request, 'odinsbane.html', {'prologue': prologue, 'chapter1': chapter1, 'chapter2': chapter2})


def poem(request):
    num_poems = Poem.objects.all().count()
    poem = Poem.objects.get(pk=np.random.randint(1,num_poems + 1))
    return render(request, 'poem.html', {'poem': poem})


def story_by_id(request, story_id):
    story = Story.objects.get(pk=story_id)
    story_link = "https://www.sigurdvidarsson.com/story/" + str(story_id)
    story_long_link = "https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.sigurdvidarsson.com%2Fstory%2F" \
        + str(story_id) \
        + "&amp;src=sdkpreparse"

    return render(request, 'story.html', {'story': story, 'story_link': story_link, 'story_long_link': story_long_link})


def author(request):
    return render(request, 'author.html')