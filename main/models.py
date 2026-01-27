from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    course = models.IntegerField(default=1)
    number_of_books = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Author(models.Model):
    class GENDER_CHOICES(models.TextChoices):
        ERKAK = 'Erkak', 'Erkak'
        AYOL = 'Ayol', 'Ayol'
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES.choices, max_length=10, blank=True, null=True)
    birth_of_date = models.DateField(null=True, blank=True)
    books = models.PositiveSmallIntegerField(blank=True, null=True)
    is_alive = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, null=True, blank=True)
    pages = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        if self.author:
            return f'{self.title}  [{self.author.name}]'
        return f'{self.title}'


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    time_of_work = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    librarian = models.ForeignKey(Librarian, on_delete=models.SET_NULL, null=True, blank=True)
    birth_off_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.student.name} [{self.book.title if self.book else "Kitob mavjud emas !"}]'
