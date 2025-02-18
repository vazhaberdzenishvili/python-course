from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def book_list(request):

    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})


def add_book(request):

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            Book = form.save()

            return redirect('book_list')
    else:
        form = BookForm()

        return render(request, 'book/add_book.html', {'form': form})
