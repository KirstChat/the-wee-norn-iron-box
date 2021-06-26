from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


def blog_posts(request):
    # A view to return blog posts
    posts = Post.objects.filter(status=1).order_by('-date_posted')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)


@login_required
def add_post(request):
    # Add blog post to site
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            form_data = post_form.save(commit=False)
            form_data.posted_by = request.user
            form_data.save()
            messages.success(request, 'Blog posted successfully!')
            return redirect('blog_posts')
        else:
            messages.error(request, 'Failed to post blog')
            return redirect('add_post')
    else:
        post_form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'post_form': post_form,
    }
    return render(request, template, context)
