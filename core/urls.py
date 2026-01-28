"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('hello/', home_view),
    path('talabalar/',talabalar_view, name='talabalar'),
    path('talabalar/<int:talaba_id>/', talaba_view),
    path('talabalar/<int:pk>/update', update_talaba_view, name='talaba-update'),
    path('mualliflar/', mualliflar_view, name='mualliflar'),
    path('mualliflar/<int:muallif_id>/', muallif_view, name='muallif-detail'),
    path('mualliflar/<int:pk>/update', update_muallif_view, name='muallif-update'),
    path('kutubxonachilar/', librarians_view, name='kutubxonachilar'),
    path('kutubxonachilar/<int:librarian_id>/', librarian_view, name='kutubxonachi'),
    path('kutubxonachilar/<int:pk>/update/', update_librarian_view, name='kutubxonachi-update'),
    path('kitoblar/', kitoblar_view, name='kitoblar'),
    path('kitoblar/<int:kitob_id>/', kitob_view),
    path('kitoblar/<int:pk>/update/', update_kitob_view, name='kitob-update'),
    path('recordlar/', records_view, name='recordlar'),
    path('recordlar/<int:record_id>/', record_view),
    path('recordlar/<int:pk>/update', record_update_view, name='record-update'),

    path('tirik-mualliflar/', live_authors),
    path('katta-kitoblar/', big_books),
    path('katta-mualliflar', authors_of_books),
    path('oxirgi-recordlar', last_records),
    path('muallifi-tirik-kitoblar', live_authors_of_books),
    path('badiiy-kitoblar', artistic_books),
    path('yoshi_katta-mualliflar', oldest_authors),
    path('kichik-mualliflar', fewer_10_books_authors),
    path('bitiruvchilar-rekordlar', graduate_students_view)
]
