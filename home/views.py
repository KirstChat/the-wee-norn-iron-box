from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ReviewForm
from .models import Review

# Create your views here.


def reviews(request):
    # A view to return reviews on the index page
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'home/index.html', context)


@login_required()
def add_review(request):
    # Add review to site
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        # Check if the review form is valid
        if review_form.is_valid():
            form_data = review_form.save(commit=False)
            form_data.posted_by = request.user
            form_data.save()
            messages.success(request, 'Review posted successfully')
            return redirect('home')
        else:
            messages.error(request, 'Failed to post review')
            return redirect('add_review')
    else:
        review_form = ReviewForm()

    template = 'home/add_review.html'
    context = {
        'review_form': review_form,
    }
    return render(request, template, context)


@login_required
def manage_reviews(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'home/manage_reviews.html', context)


@login_required
def delete_review(request, review_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only the admin can delete reviews.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('manage_reviews'))
