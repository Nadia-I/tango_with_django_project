from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category
from rango.models import Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Nadia Issouquaein'}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        context_dict['category'] = category
    
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
        # Go render the response and return it to the client.
    
    return render(request, 'rango/category.html', context=context_dict)