from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "recordapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/create", views.post_create, name="post"),
    path("post/<slug:slug>/", views.detail, name="detail"),
    path("post/<slug:slug>/update", views.detail_update, name="detail_update"),
    path("post/<slug:slug>/delete", views.detail_delete, name="detail_delete"),
    
    
]

