from django.contrib import admin

# Register your models here.
from .models import Haiku, Chapter, Poem, Story
admin.site.register(Haiku)
admin.site.register(Chapter)
admin.site.register(Poem)
admin.site.register(Story)