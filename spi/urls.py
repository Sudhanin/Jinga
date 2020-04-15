from django.urls import path
from . import views
urlpatterns = [
    path('post/',views.post,name='post'),
    path('publish/',views.publish,name='publish')
]