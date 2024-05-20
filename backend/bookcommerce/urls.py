from django.urls import path, include
from . import views
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='bookcommerce-book-detail'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
]