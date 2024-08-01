from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index_page),
    path('catalog/', views.product_view, name='products'),
    path('search/<slug:slug>/', views.product_detail_view, name='one_category'),
    path('<slug:slug>/', views.product_detail_view, name='product'),

]
