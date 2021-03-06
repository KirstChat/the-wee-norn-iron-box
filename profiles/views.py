from django.contrib import messages
from django.shortcuts import get_object_or_404, render

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from blog.models import Post


def profile(request):
    # Display the user's profile
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Failed to update profile.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    posts = Post.objects.filter(status=0).order_by('-date_posted')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'posts': posts,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        f'This is a past order for {order_number} placed on {order.date}.')

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
