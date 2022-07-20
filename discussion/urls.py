
from django.urls import path
from .views import likepost, postview,unlikepost,AddComment
urlpatterns = [
    path('<int:id>', postview,name='post'),
    path('like/<int:id>',likepost,name='likepost'),
    path('unlike/<int:id>',unlikepost,name='unlikepost'),
    path('addcomment/<int:id>',AddComment.as_view(),name='addcomment')
]
