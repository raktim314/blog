from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import CommentForm, BlogForm


def home(request):
    return render(request, 'blog/index.html')


def blog(request):
    return render(request, 'blog/blog.html')


def post_detail(request):
    return render(request, 'blog/post_detail.html')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})