from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
# Create your views here.


def index(request):
    post = Post.objects.GET.get.all()
    return render(request, 'posts/index.html')


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)


def detail(request, id):
    pass


def update(request, id):
    pass


def delete(request, id):
    pass
