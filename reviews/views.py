from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Review

# Create your views here.


def all_reviews(request):
    # A view to display all reviews
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)


@login_required()
def add_review(request):
    # Add review to site

    return render(request)
