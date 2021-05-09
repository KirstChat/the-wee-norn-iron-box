from django.shortcuts import render

# Create your views here.


def view_box(request):
    # A view that renders the box contents

    return render(request, 'box/box.html')
