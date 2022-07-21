from unicodedata import category
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, Comment, Post

# Create your views here.

def postview(request,id):
    post=get_object_or_404(Post,pk=id)
    categories=Category.objects.all()
    print(post.commentpost.all)
    if request.user in post.like.all():
        print('ssssssssssss')
    
    return render(request,'discussion/post.html',{'title':'my title','post':post,'categories':categories,'comments':post.commentpost.all().order_by('-createdat')})
@login_required
def likepost(request,id):
    post=get_object_or_404(Post,pk=id)
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        messages.success(request, post.title + " has been removed from your WishList")
    else:
        post.like.add(request.user)
        messages.success(request, "Added " + post.title + " to your WishList") 
        
    return HttpResponseRedirect(request.META["HTTP_REFERER"])       
    
@login_required
def unlikepost(request,id):
    post=get_object_or_404(Post,pk=id)
    if post.unlike.filter(id=request.user.id).exists():
        post.unlike.remove(request.user)
    else:
        post.unlike.add(request.user)
        
    return HttpResponseRedirect(request.META["HTTP_REFERER"])       
        
class AddComment(LoginRequiredMixin,CreateView):
    
    model=Comment
    fields=('content','user','post')
    template_name='discussion/addcomment.html'
    success_url='/books/index/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post=get_object_or_404(Post,pk=self.kwargs['id'])
        return super().form_valid(form)
    def get_context_data(self,*args, **kwargs):
        context = super(AddComment, self).get_context_data(*args,**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
# ------------------------searchPost------------------------
def searchPost(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title=searched)
        categories = Post.objects.filter(category__name=searched)
        context = {'searched':searched, 'posts':posts, 'categories':categories}
        
        return render(request, 'discussion/search.html',context)
    else:
        return render(request, 'discussion/search.html',{})

# ----------------------------footer------------------------------------
# Home Page Posts 
def loadingPages(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by('-createdat')
    
    # number posts in page
    num_of_posts=5
    p= Paginator(Post.objects.order_by('-createdat'), num_of_posts)
    page= request.GET.get('page')
    pagination_posts=p.get_page(page)

    # To show num of pages (1,2,3,...)
    nums= "a" * pagination_posts.paginator.num_pages
    pages=pagination_posts
    context = {'posts': posts,'categories': categories,'pages':pages ,'nums':nums}
    # ------------change search page to home page-------------------
    return render(request, 'discussion/search.html', context)
 
