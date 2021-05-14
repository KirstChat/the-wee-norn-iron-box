from django.shortcuts import render

from reviews.models import Review

# Create your views here.


def index(request):
    # A view to return the index page
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'home/index.html', context)
