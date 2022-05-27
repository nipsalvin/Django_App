from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Book

def index(requst):
    return HttpResponse ("""
    Hello world
    """)

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return HttpResponse(f"Book: {book.title}, published on {book.pub_date}")
