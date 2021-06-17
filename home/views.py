from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ReviewForm
from .models import Review

# Create your views here.


def reviews(request):
    # A view to return reviews the index page
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'home/index.html', context)


@login_required()
def add_review(request):
    # Add review to site
    if request.method == 'POST':
        review_form = ReviewForm(request.POST or None)

        # Check if the form is valid
        if review_form.is_valid():
            form_data = review_form.save(commit=False)
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
