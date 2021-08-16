from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('writing/', views.index, name='writing'),
     path('haiku/<int:haiku_id>', views.haiku_by_id, name='haiku_by_id'),
     path('odinsbane', views.odinsbane, name='odinsbane'),
     path('poem', views.poem, name='poem'),
     path('author', views.author, name='author')
]