from django.urls import path, include
from . import views
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='bookcommerce-book-detail'),
]
