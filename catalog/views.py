from django.shortcuts import render
# from django.http import HttpResponse
from .models import Book,Author,Genre,BookInstance
def index(request):
    num_books= Book.objects.all().count()
    num_authors= Author.objects.count()
    num_instances= BookInstance.objects.all().count()
    num_instances_available= BookInstance.objects.filter(status__exact='a').count()
    num_visits= request.session.get('num_visits' ,0)
    request.session['num_visits'] = num_visits +1
    context={
        'num_books': num_books,
        'num_authors': num_authors,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_visits' : num_visits,
    }
    return render(request, 'index.html', context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by=2

class BookDetailView(generic.DetailView):
    model=Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

