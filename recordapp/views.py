from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Post
from .forms import PostForm 

class IndexView(View):
    def get(self, request):
        # posts = Post.objects.all()  # データベースから全てのPostを取得
        posts = Post.objects.order_by("-date")  # データベースから全てのPostを取得
        return render(request, "recordapp/index.html", {"posts": posts})

class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, "recordapp/index_form.html", {"form":form})
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("recordapp:index")
        return render(request, "recordapp/index_form.html", {"form":form})
        
class PostDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, "recordapp/detail.html", {"post": post})
        

index = IndexView.as_view()
post_create =  PostCreateView.as_view()
detail = PostDetailView.as_view()
