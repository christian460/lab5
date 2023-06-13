from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.shortcuts import get_object_or_404


def index(request):
    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)

def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'template/catalog/book_detail.html', context={'book': book})

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    
    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
    context_object_name = 'book_list'
    template_name = 'templates/catalog/book_list.html'


class BookDetailView(generic.DetailView):
    model = Book


    