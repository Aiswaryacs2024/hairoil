from django.urls import path
from .views import (
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    login_view,
    logout_view,
    register_view
)

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]
