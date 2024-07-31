from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def index_page(request):
    return render(request, 'shop/index.html')
