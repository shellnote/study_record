from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Post, Category
from .forms import PostForm 
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    def get(self, request):
        # posts = Post.objects.all()  # データベースから全てのPostを取得
        posts = Post.objects.order_by("-date")  # データベースから全てのPostを取得
        return render(request, "recordapp/index.html", {"posts": posts})

class PostCreateView(LoginRequiredMixin,View):
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
    
class PostUpdateView(LoginRequiredMixin,View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = PostForm(instance=post)
        return render(request, "recordapp/detail_update.html", {"form": form})
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("recordapp:detail", slug=slug)
        return render(request, "recordapp/index_form.html", {"form":form})

class PostDeleteView(LoginRequiredMixin,View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, "recordapp/detail_delete.html", {"post": post})
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect("recordapp:index")

class CategoryListView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        posts = Post.objects.filter(category=category)
        context = {
            "category": category,
            "posts": posts  
        }
        return render(request, "recordapp/category_list.html", context)
        

index = IndexView.as_view()
post_create =  PostCreateView.as_view()
detail = PostDetailView.as_view()
detail_update = PostUpdateView.as_view()
detail_delete = PostDeleteView.as_view()
category_list = CategoryListView.as_view()
