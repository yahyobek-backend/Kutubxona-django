from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .forms import *


def home_view(request):
    return HttpResponse("""
    <h1>Welcome to Home Page View</h1>
    <p>This is the main landing page of the website.</p>
    """)


def home_page(request):
    return render(request, 'index.html')


def talabalar_view(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get('ism'),
            group=request.POST.get('guruh'),
            course=request.POST.get('kurs') if request.POST.get('kurs') != "" else 1,
            number_of_books=request.POST.get('kitob_soni') if request.POST.get('kitob_soni') != "" else 0,
        )
        return redirect('talabalar')

    talabalar = Student.objects.order_by('name')

    context = {
        'talabalar': talabalar
    }
    return render(request, 'talabalar.html', context)

def talaba_view(request, talaba_id):
    student = Student.objects.get(id=talaba_id)

    context = {
        'student': student
    }
    return render(request, 'talaba-details.html', context)

def update_talaba_view(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == "POST":
        student.name = request.POST.get('ism')
        student.group = request.POST.get('guruh')
        student.course = request.POST.get('kurs')
        student.number_of_books = request.POST.get('kitob_soni')
        student.save()
        return redirect('talabalar')

    context={
        'student': student
    }
    return render(request, 'talaba-update.html', context)

def mualliflar_view(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mualliflar')

    mualliflar = Author.objects.order_by('name')

    context = {
        'mualliflar': mualliflar,
        'form': form
    }
    return render(request, 'mualliflar.html', context)



def muallif_view(request, muallif_id):
    author = Author.objects.get(id=muallif_id)

    context = {
        'author': author
    }
    return render(request, 'muallif-details.html', context)

from datetime import datetime

def update_muallif_view(request, pk):
    author = get_object_or_404(Author, id=pk)

    if request.method == "POST":
        # 't_sana' dan sana olish
        birth_date_str = request.POST.get('t_sana')
        birth_date = None
        if birth_date_str:
            try:
                birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
            except ValueError:
                birth_date = None  # Agar noto'g'ri format bo'lsa, None qo'y

        # Yangilash
        Author.objects.filter(id=pk).update(
            name=request.POST.get('ism', ''),
            gender=request.POST.get('jins', ''),
            birth_of_date=birth_date,  # To'g'ri formatda
            books=request.POST.get('kitob_soni', None),
            is_alive=request.POST.get('tirik') == 'on'  # Checkbox: 'on' bo'lsa True
        )
        return redirect('mualliflar')

    context = {
        "author": author
    }
    return render(request, 'author-update.html', context)



def kitoblar_view(request):
    if request.method == 'POST':

        Book.objects.create(
            title=request.POST.get('nom'),
            genre=request.POST.get('janr'),
            pages=request.POST.get('sahifa'),
            author=Author.objects.get(id=request.POST.get('muallif_id')),
        )
        return redirect('kitoblar')
    kitoblar = Book.objects.order_by('title')
    mualliflar = Author.objects.order_by('name')
    context = {
        'kitoblar': kitoblar,
        'mualliflar': mualliflar,
    }
    return render(request, 'kitoblar.html', context)

def kitob_view(request, kitob_id):
    book = Book.objects.get(id=kitob_id)

    context = {
        'book': book
    }
    return render(request, 'kitob-details.html', context)

def update_kitob_view(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == "POST":
        book.title = request.POST.get('nom')
        book.genre = request.POST.get('janr')
        book.pages = request.POST.get('sahifa')
        book.author = get_object_or_404(Author, id=request.POST.get('muallif_id'))
        book.save()   # MUHIM: o‘zgarishlarni bazaga saqlash
        return redirect('kitoblar')

    # Agar GET bo‘lsa, formani ko‘rsatish
    authors = Author.objects.all().order_by('name')
    context = {
        'book': book,
        "authors": authors
    }
    return render(request, 'kitob-update.html', context)


def librarians_view(request):
    if request.method == "POST":
        Librarian.objects.create(
            name=request.POST.get('ism'),
            time_of_work=request.POST.get('ish_vaqti'),
        )
        return redirect('kutubxonachilar')
    librarians = Librarian.objects.all()
    context = {
        'librarians': librarians
    }

    return render(request, 'librarians.html', context)

def librarian_view(request, librarian_id):
    librarian = Librarian.objects.get(id=librarian_id)

    context = {
        'librarian': librarian
    }
    return render(request, 'librarian-details.html', context)

def update_librarian_view(request, pk):
    librarian = get_object_or_404(Librarian, id=pk)

    if request.method == "POST":
        librarian.name = request.POST.get('ism')
        librarian.time_of_work = request.POST.get('ish_vaqti')
        librarian.save()
        return redirect('kutubxonachilar')

    context = {
        'librarian': librarian
    }
    return render(request, 'librarian-update.html', context)


def records_view(request):
    form = RecordForm()
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('recordlar')

    context = {
            "records": Record.objects.all(),
            "talabalar": Student.objects.all(),
            "kitoblar": Book.objects.all(),
            "librarians": Librarian.objects.all(),
            'form': form
        }
    return render(request, "records.html", context)

def record_view(request, record_id):
    record = Record.objects.get(id=record_id)

    content = {
        'record': record
    }
    return render(request, 'record-details.html', content)

def record_update_view(request, pk):
    record = get_object_or_404(Record, id=pk)
    if request.method == "POST":
        record.student = get_object_or_404(Student, id=request.POST.get('student_id'))
        record.book = get_object_or_404(Book, id=request.POST.get('book_id'))
        record.librarian = get_object_or_404(Librarian, id=request.POST.get('librarian_id'))
        record.birth_off_date = request.POST.get('olingan_sana')
        record.return_date = request.POST.get('qaytariladigan_sana')
        record.save()
        return redirect('recordlar')
    students = Student.objects.all().order_by('name')
    books = Book.objects.all().order_by('title')
    librarians = Librarian.objects.all().order_by('name')
    content = {
        'record': record,
        'students': students,
        'books': books,
        'librarians': librarians
    }
    return render(request, 'record-update.html', content)

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


def graduate_students_view(request):
    records = Record.objects.filter(student__course=4)

    content = {
        'records': records
    }
    return render(request, 'graduate_students.html', content)
