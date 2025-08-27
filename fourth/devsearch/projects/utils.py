from .models import Project
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_projects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    pr = Project.objects.filter(  # Запрос к базе данных и поиск
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query)
    )

    return pr, search_query


def paginate_projects(request, pr, results):
    page = request.GET.get('page')
    # results = 3  # Указали количество проектов на 1 странице
    paginator = Paginator(pr, results)
    # обработка случаев
    try:
        pr = paginator.page(page)
    except PageNotAnInteger:
        page = 1  # Выводит на первую страницу
        pr = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages  # Выводит на последнюю страницу
        pr = paginator.page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(1, right_index)
    return custom_range, pr
