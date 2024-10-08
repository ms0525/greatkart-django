from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_items/<int:product_id>/', views.remove_cart_items, name='remove_cart_items'),
    #path('<slug:category_slug>/', views.carts, name='products_by_category'),
    #path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
