from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('products/', views.ProductView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),

    path('categories/', views.CategoriesView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)