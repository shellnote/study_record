from django.urls import path
from .import views

app_name = "recordapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/create", views.post_create, name="post"),
    
]
