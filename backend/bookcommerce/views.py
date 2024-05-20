from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Book, Cart, CartItem
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun {username} berhasil dibuat! Silakan log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'bookcommerce/register.html', {'form': form})

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

class BookListView(ListView):
    model = Book
    template_name = 'bookcommerce/index.html'
    context_object_name = 'books'
    ordering = ['title']

class BookDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        book = Book.objects.get(pk=pk)
        self.current_book = book

        context = {
            'book': book,
        }

        return render(request, 'bookcommerce/book_detail.html', context)

@login_required
def add_to_cart(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided
        cart, created = Cart.objects.get_or_create(customer=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        messages.success(request, f"Berhasil menambahkan {quantity} {book.title}(s) ke dalam keranjang!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))
    else:
        return HttpResponseRedirect(reverse('home'))  # Redirect if not a POST request

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(customer=request.user)
    return render(request, 'bookcommerce/cart_detail.html', {'cart': cart})