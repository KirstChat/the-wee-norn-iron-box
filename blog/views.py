from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import CommentForm, PostForm


def blog_posts(request):
    # A view to return all blog posts
    posts = Post.objects.filter(status=1).order_by('-date_posted')
    drafts = Post.objects.filter(status=0).order_by('-date_posted')

    context = {
        'posts': posts,
        'drafts': drafts,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, post_id):
    # A view to display an individual blog post
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(post=post_id).order_by('-date_commented')

    new_comment = None

    # Add a comment to a post
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.posted_by = request.user
            new_comment.save()
            messages.success(request, 'Comment successfully posted')
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'new_comment': new_comment,
    }

    return render(request, 'blog/post_detail.html', context)


@login_required
def add_post(request):
    # Add blog post
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


@login_required
def edit_post(request, post_id):
    # Edit a blog post
    post = get_object_or_404(Post, pk=post_id)

    if request.user != post.posted_by:
        messages.error(
            request, 'Only the user that posted this post can edit it!'
        )
        return redirect(reverse('blog_posts'))

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(
                request, f'Successfully updated {post.title} post')
            return redirect('blog_posts')
        else:
            messages.error(request, f'Failed to update {post.title}')
    else:
        post_form = PostForm(instance=post)
        messages.info(request, f'You are currently editing {post.title}')

        template = 'blog/edit_post.html'
        context = {
            'post_form': post_form,
            'post': post,
        }

        return render(request, template, context)


@login_required
def delete_post(request, post_id):
    # Delete a blog post
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.posted_by:
        messages.error(
            request, 'Only the user that posted this post can delete it!'
        )
        return redirect(reverse('blog_posts'))
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog_posts'))
