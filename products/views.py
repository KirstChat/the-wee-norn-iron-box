from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def all_products(request):
    # A view to show all products

    products = Product.objects.all()
    query = None
    categories = None

    # Filter/Search Queries
    if request.GET:
        # Filter Products by Category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Search Products
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Sorry, we couldn't find that product!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def add_product(request):
    # Add a new product
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
