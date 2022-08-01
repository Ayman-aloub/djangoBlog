
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/<int:blog_id>/', views.blog_topics, name='blog_topics'),
    path('blogs/<int:blog_id>/new/', views.new_topic, name='new_topic'),
   
]
