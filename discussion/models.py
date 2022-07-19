from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    user=models.ManyToManyField(User,related_name='subscribe')
    


class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    image=models.ImageField(upload_to='images')
    user=models.ForeignKey(User,related_name='postuser',on_delete=models.CASCADE)
    category=models.ForeignKey(Category,related_name='postcategory',on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)
    like=models.ManyToManyField(User,related_name='likepost')
    unlike=models.ManyToManyField(User,related_name='unlikepost')
class Comment(models.Model):
    content=models.TextField()
    user=models.ForeignKey(User,related_name='commentuser',on_delete=models.CASCADE)
    post=models.ForeignKey(Post,related_name='commentpost',on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)
        

class Reply(models.Model):
    content=models.TextField()
    user=models.ForeignKey(User,related_name='replyuser',on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment,related_name='replycomment',on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)
         