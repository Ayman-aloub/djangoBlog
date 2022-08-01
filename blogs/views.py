from email import message
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse
from blogs.models import Blog, Topic , Post
from django.contrib.auth.models import User
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


def blog_topics(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'topics.html', {'blog': blog})

@login_required
def new_topic(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    form = NewTopicForm()
    #user= User.objects.first()
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.blog = blog
            topic.created_by = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                created_by=request.user,
                topic=topic
            )
            return redirect('blog_topics',blog_id=blog.id)
    else:
        form = NewTopicForm()    
    return render(request,'new_topic.html',{'blog': blog,'form':form})


