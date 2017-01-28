from django.contrib import admin
from .models import Post

admin.site.register(Post)
# Register your models here.
#This makes the model visible on the admin page.
