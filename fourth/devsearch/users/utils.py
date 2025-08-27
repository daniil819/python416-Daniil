from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_profiles(request, pr, results):
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


def search_profile(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    prof = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )

    return prof, search_query
