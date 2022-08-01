from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Blog , Topic
# Register your models here.
admin.site.register(Blog)
admin.site.register(Topic)
admin.site.unregister(Group)

admin.site.site_header = "Django Blogs Admin Panel"
admin.site.site_title = "Blogs Admin Panel"
