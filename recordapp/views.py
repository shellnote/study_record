from django.shortcuts import render
from django.views import View
from .models import Post

class IndexView(View):
    def get(self, request):
        posts = Post.objects.all()  # データベースから全てのPostを取得
        return render(request, "recordapp/index.html", {"posts": posts})

index = IndexView.as_view()