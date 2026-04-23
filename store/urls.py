from django.urls import path
from . import views

urlpatterns = [
    # Главная - все товары
    path('', views.ProductListView.as_view(), name='product_list'),
    # Товары по категории
    path('category/<slug:category_slug>/', views.ProductListView.as_view(), name='product_list_by_category'),
    # Просмотр товара
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    # Добавление товара
    path('add/new/', views.ProductCreateView.as_view(), name='product_add'),
    # Редактирование товара
    path('product/<slug:slug>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
]