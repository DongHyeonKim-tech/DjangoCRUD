from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import BidCrawling
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect
from .forms import BookCreateForm, BookUpdateForm
# Create your views here.


class Index(generic.ListView):
    model = BidCrawling
    paginate_by = 100
    context_object_name = 'books'
    template_name = 'index.html'


class BookDetailView(generic.DetailView):
    model = BidCrawling
    template_name = 'book/read_book.html'
    context_object_name = 'book_detail'


class BookCreateView(generic.CreateView):
    model = BidCrawling
    form_class = BookCreateForm
    success_url = reverse_lazy('index')
    template_name = 'book/create_book.html'


class BookUpdateView(generic.UpdateView):
    model = BidCrawling
    form_class = BookUpdateForm
    context_object_name = 'update_book'
    success_url = reverse_lazy('index')
    template_name = 'book/update_book.html'


class BookDeleteView(generic.DeleteView):
    model = BidCrawling
    context_object_name = 'delete_book'
    success_url = reverse_lazy('index')
    template_name = 'book/delete_book.html'
