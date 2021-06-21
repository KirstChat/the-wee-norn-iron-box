from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    # Add a new product
    if not request.user.is_superuser:
        messages.error(request, 'Only the admin can add new products.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to add new product.\
                Please check that your form is valid')
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    # Edit an existing product

    if not request.user.is_superuser:
        messages.error(request, 'Only the admin can edit products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect('products')
        else:
            messages.error(request, f'Failed to update {product.name}')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are currently editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    # Delete an existing product
    if not request.user.is_superuser:
        messages.error(request, 'Only the admin can delete products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
