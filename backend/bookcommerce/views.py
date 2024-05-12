from django.shortcuts import render, redirect
from django.views.generic import ListView, View, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Book
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