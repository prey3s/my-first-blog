from django.conf.urls import url
from . import views #We are importing Django's function url and all of our views
#from the blog application.

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
] #adding our first URL pattern
