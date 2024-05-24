from django.urls import path, include
from . import views
from .views import BookListView, BookDetailView, add_to_cart, cart_detail, update_cart_item, delete_cart_item, delete_all_cart_items, CartStaticView, SearchView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='bookcommerce-book-detail'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart-static/', CartStaticView.as_view(), name='cart_detail_static'),
    path('cart/update/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('cart/delete-item/<int:item_id>/', delete_cart_item, name='delete_cart_item'),
    path('cart/delete-all/', delete_all_cart_items, name='delete_all_cart_items'),
    path('search', SearchView.as_view(), name='search')
]