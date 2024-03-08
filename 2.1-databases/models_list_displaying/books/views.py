from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book
from datetime import datetime

def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    if pub_date:
        try:
            pub_date_obj = datetime.strptime(pub_date, '%Y-%m-%d')
            # Фильтрация книг по дате публикации
            books = Book.objects.filter(pub_date=pub_date_obj)
        except ValueError:
            # Если преобразование не удалось, возвращаем ошибку или все книги
            books = Book.objects.all()
    else:
        # Получение всех книг
        books = Book.objects.all()

    # Получение списка уникальных дат публикации
    pub_dates = Book.objects.dates('pub_date', 'day')

    # Пагинация
    paginator = Paginator(books, 10) # Пример: 10 книг на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Определение текущей даты и предыдущей/следующей даты
    if pub_date:
        pub_date_obj = datetime.strptime(pub_date, '%Y-%m-%d')
        prev_date = Book.objects.filter(pub_date__lt=pub_date_obj).order_by('-pub_date').first().pub_date if Book.objects.filter(pub_date__lt=pub_date_obj).exists() else None
        next_date = Book.objects.filter(pub_date__gt=pub_date_obj).order_by('pub_date').first().pub_date if Book.objects.filter(pub_date__gt=pub_date_obj).exists() else None
    else:
        prev_date = None
        next_date = None

    context = {
        'books': page_obj,
        'pub_dates': pub_dates,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    return render(request, template, context)


