from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for the home page of the site"""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_genres = Genre.objects.count()

    books_with_the = 0 # a list of books with the word 'the' in the title (case insensitive)

    for book in Book.objects.all():
        if "the" in book.title.lower():
            books_with_the += 1

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Note, all() is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'books_with_the': books_with_the
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
    num_instances = BookInstance.objects.all().count()
