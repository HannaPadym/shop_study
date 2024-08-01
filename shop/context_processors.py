from .models import Category, ProxyProduct


def categories(request):
    categories = Category.objects.filter(parent=None)
    return {'categories': categories}


