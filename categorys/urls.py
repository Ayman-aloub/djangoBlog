from django.urls import path
from . import views

app_name = 'categorys'
urlpatterns = [
    path('category/',views.index,name='index'),
    path('category_details/<int:id>/',views.category_details,name='category_details'),
]