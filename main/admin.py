from django.contrib import admin
from main.models import Student, Author, Record, Book, Librarian

# Register your models here.

admin.site.register(Student)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Librarian)
admin.site.register(Record)