from django.shortcuts import render
from django.views import generic

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


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        context['some_data'] = 'test data'
        return context


class BookDetailView(generic.DetailView):
    model = Book



class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5


class AuthorDetailView(generic.DetailView):
    model = Author
