from pyexpat import model
from django.shortcuts import render
from .models import Category

# Create your views here.
def index(request):
	category = Category.objects.all()
	return render(request,'index.html',context={"categorys":category})
	

def cotactus(request):
	
	return render(request,'cotactus.html')

def category_details(request,id):
    category = Category.objects.get(pk=id)
   
    return render(request,'index.html',context={"categorys":category})