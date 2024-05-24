from django.urls import path, include
from . import views
from .views import BookListView, BookDetailView, add_to_cart, cart_detail, update_cart_item, delete_cart_item, delete_all_cart_items, checkout, payment, profile, order_history, create_address, update_address, change_password, search, CartStaticView, SearchView, OrderStaticView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='bookcommerce-book-detail'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart-static/', CartStaticView.as_view(), name='cart_detail_static'),
    path('cart/update/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('cart/delete-item/<int:item_id>/', delete_cart_item, name='delete_cart_item'),
    path('cart/delete-all/', delete_all_cart_items, name='delete_all_cart_items'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', payment, name='payment'),
    path('profile/', profile, name='profile'),
    path('order_history/', views.order_history, name='order_history'),
    path('address/create/', create_address, name='create_address'),
    path('address/update/<int:address_id>/', update_address, name='update_address'),
    path('profile/change-password/', change_password, name='change_password'),
    path('search', SearchView.as_view(), name='search'),
    path('order', OrderStaticView.as_view(), name='order_static')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)