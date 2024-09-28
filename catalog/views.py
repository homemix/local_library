from django.shortcuts import render

from .models import Author, Book, BookInstance, Genre


def index(request):
    """View Function for home page of site"""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books
    num_instances_available = BookInstance.objects.all().filter(status__exact='a').count()

    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_books_with_soldier = Book.objects.filter(summary__icontains='soldier').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_with_soldier': num_books_with_soldier,
    }

    return render(request, template_name='index.html', context=context)
