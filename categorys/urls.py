from django.urls import path
from . import views

app_name = 'categorys'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('category_details/<int:id>/',views.category_details,name='category_details'),
    path('contactus/',views.cotactus,name='contactus'), 
    path('aboutus/',views.aboutus,name='aboutus'), 
]