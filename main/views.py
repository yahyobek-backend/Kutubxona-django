from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *


def home_view(request):
    return HttpResponse("""
    <h1>Welcome to Home Page View</h1>
    <p>This is the main landing page of the website.</p>
    """)


def home_page(request):
    return render(request, 'index.html')


def talabalar_view(request):
    talabalar = Student.objects.all()

    context = {
        'talabalar': talabalar
    }
    return render(request, 'talabalar.html', context)


def mualliflar_view(request):
    mualliflar = Author.objects.all()

    context = {
        'mualliflar': mualliflar
    }
    return render(request, 'mualliflar.html', context)


def talaba_view(request, talaba_id):
    student = Student.objects.get(id=talaba_id)

    context = {
        'student': student
    }
    return render(request, 'talaba-details.html', context)


def muallif_view(request, muallif_id):
    author = Author.objects.get(id=muallif_id)

    context = {
        'author': author
    }
    return render(request, 'muallif-details.html', context)


def kitoblar_view(request):
    kitoblar = Book.objects.all()
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'kitoblar.html', context)

def librarians_view(request):
    librarians = Librarian.objects.all()
    context = {
        'librarians': librarians
    }

    return render(request, 'librarians.html', context)

def kitob_view(request, kitob_id):
    book = Book.objects.get(id=kitob_id)

    context = {
        'book': book
    }
    return render(request, 'kitob-details.html', context)


def records_view(request):
    records = Record.objects.all()
    context = {
        'records': records
    }
    return render(request, 'records.html', context)


def live_authors(request):
    authors = Author.objects.filter(is_alive=True)
    context = {
        'authors': authors
    }

    return render(request, 'live_authors.html', context)


def big_books(request):
    books = Book.objects.order_by('-pages')[:3]
    context = {
        'books': books
    }
    return render(request, 'big_books.html', context)


def authors_of_books(request):
    books = Author.objects.order_by('-books')[:3]
    context = {
        'books': books
    }
    return render(request, 'author_of_books.html', context)


def last_records(request):
    records = Record.objects.order_by('-birth_off_date')[:3]
    context = {
        'records': records
    }
    return render(request, 'last_records.html', context)


def live_authors_of_books(request):
    books = Book.objects.filter(author__is_alive=True)
    content = {
        'books': books
    }
    return render(request, 'live_authors_of_books.html', content)

def artistic_books(request):
    books = Book.objects.filter(genre='badiiy')
    content = {
        'books': books
    }
    return render(request, 'artistic_books.html', content)

def oldest_authors(request):
    authors = Author.objects.order_by('birth_of_date')[:3]
    content = {
        'authors': authors
    }
    return render(request, 'oldest_authors.html', content)

def fewer_10_books_authors(request):
    authors = Author.objects.filter(books__lt=10)
    content = {
        'authors': authors
    }
    return render(request, 'fewer_10_books_authors.html', content)

def record_view(request, record_id):
    record = Record.objects.get(id=record_id)

    content = {
        'record': record
    }
    return render(request, 'record-details.html', content)

def graduate_students_view(request):
    records = Record.objects.filter(student__course=4)

    content = {
        'records': records
    }
    return render(request, 'graduate_students.html', content)
