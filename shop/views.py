from django.shortcuts import render, get_object_or_404
from .models import Category, ProxyProduct

# Create your views here.
from django.urls import reverse


def index_page(request):
    return render(request, 'shop/index.html')


def product_view(request):
    products = ProxyProduct.objects.all()
    return render(request, 'shop/products.html', {'products': products})


def product_detail_view(request, slug):
    product = get_object_or_404(ProxyProduct, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = ProxyProduct.objects.select_related('category').filter(category=category)
    context = {'products': products, 'category': category}
    return render(request, 'shop/category_list.html', context)


