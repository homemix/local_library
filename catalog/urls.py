from django.urls import path

from catalog import views
from catalog.views import BookListView,BookDetailView,AuthorListView,AuthorDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('books/',BookListView.as_view(), name='books'),
    path('authors/',AuthorListView.as_view(), name='authors'),
    path('books/<int:pk>',BookDetailView.as_view(), name='book-detail'),
    path('authors/<int:pk>',AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedBooksByLibrarian.as_view(), name='librarian-borrowed'),
]