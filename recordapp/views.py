from django.shortcuts import render,redirect
from django.views import View
from .models import Post
from .forms import PostForm 

class IndexView(View):
    def get(self, request):
        posts = Post.objects.all()  # データベースから全てのPostを取得
        return render(request, "recordapp/index.html", {"posts": posts})

class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, "recordapp/index_form.html", {"form":form})
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recordapp:index")
        return render(request, "recordapp/index_form.html", {"form":form})
        

index = IndexView.as_view()
post_create =  PostCreateView.as_view()