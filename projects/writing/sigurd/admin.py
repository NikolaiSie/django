from django.contrib import admin

# Register your models here.
from .models import Haiku, Chapter, Poem
admin.site.register(Haiku)
admin.site.register(Chapter)
admin.site.register(Poem)