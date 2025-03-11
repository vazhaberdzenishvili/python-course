from django.shortcuts import redirect, get_object_or_404
from .models import Book, BookCart
from .forms import BookForm
from django.db.models import Q
import logging
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from .mixins import AddBookMixin, UpdateBookMixin, DeleteBookMixin
from django.contrib.auth.mixins import LoginRequiredMixin

logger = logging.getLogger(__name__)


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    paginate_by = 3

    def get_queryset(self):

        title_query = self.request.GET.get('search_by_title')
        genre_query = self.request.GET.get('search_by_genre')

        logger.warning(
            f"Filtering: Title - {title_query}, Genre - {genre_query}")
        filters = Q()

        if title_query:
            filters |= Q(title__icontains=title_query)

        if genre_query:
            filters |= Q(genre__icontains=genre_query)

        if title_query and genre_query:
            filters &= Q(title__icontains=title_query) & Q(
                genre__icontains=genre_query)

        if filters:
            books = Book.objects.filter(filters).order_by("title")
        else:
            books = Book.objects.all().order_by("title")
        return books


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/book_detail.html'


class CreateBookView(AddBookMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/add_book.html'
    success_url = reverse_lazy('core:book_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        Book = form.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class BookUpdateView(UpdateBookMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/update_book.html'
    login_url = reverse_lazy('login')

    def get_success_url(self):
        success_url = reverse_lazy('core:book_detail', kwargs={
                                   'pk': self.object.pk})
        return success_url


class BookDeleteView(DeleteBookMixin, DeleteView):
    model = Book
    template_name = 'book/confirm_delete.html'
    success_url = reverse_lazy('core:book_list')
    login_url = reverse_lazy('login')


class BookPurchaseView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        if book.is_sold_out():
            messages.error(request, 'Book not available')
            return redirect('core:book_list')

        item = BookCart.objects.filter(book=book, user=request.user).first()

        if item:
            messages.error(
                request, 'You have already added this book to your cart')
        else:
            book_cart = BookCart.objects.create(
                book=book, user=request.user, book_count=1)
            book.book_count -= 1
            book.save()
            messages.success(
                request, f'Successfully added {book.title} to your cart!')

        send_mail(
            'Book Purchase Confirmation',
            f'{request.user.username} has successfully added book: {book.title} by {book.author} to their cart.',
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            fail_silently=False
        )

        return redirect('core:book_list')
