from datetime import date

from django.shortcuts import render

from django.db.models import Value, Q, Count, Avg, Sum, F, CharField
from django.db.models.functions import Concat, Cast

from .models import GenreMovie, Artist, Movie, Comment


# def home(request):
    # queryset = Movie.objects.annotate(price=F("year")*1.1, alaki=Concat(Value("alaki "), Cast(F("rating"), output_field=CharField())))
    # # queryset = Movie.objects.annotate(price=F("year")*1.1, alaki=Concat(Value("alaki "), F("rating"), output_field=CharField()))
    # queryset = Comment.objects.only("id", "user")
    # queryset = Comment.objects.only("id", "user", "text", "is_active")
    # queryset = Comment.objects.defer("movie")
    # queryset = Comment.objects.values("id", "user", "text", "is_active")
    # queryset = Comment.objects.values("id", "user")
    # queryset = Comment.objects.values_list("id", "user", "text", "is_active")
    # queryset = Comment.objects.values_list("text")
    # queryset = Comment.objects.values_list("text", flat=True)
    # queryset = Movie.objects.aggregate(Avg("rating"))
    # queryset = Movie.objects.aggregate(avg=Avg("rating"))
    # queryset = Movie.objects.aggregate(Sum("rating"))
    # queryset = Movie.objects.aggregate(s=Sum("rating"))
    # queryset = Movie.objects.aggregate(Count("rating"))
    # queryset = Movie.objects.count()
    # queryset = Comment.objects.get(id=10)
    # queryset = Comment.objects.raw("SELECT * FROM movies.Artist WHERE firs_name='Ali';")
    # first last earlieast latest order_by
    # queryset = Comment.objects.filter(user="Sanaz Ferdosi").first()
    # queryset = Comment.objects.filter(user="Sanaz Ferdosi").order_by("text").first()
    # queryset = Comment.objects.filter(user="Sanaz Ferdosi").earliest("text")
    # queryset = Comment.objects.filter(user="Sanaz Ferdosi fffff").earliest("text")
    # queryset = Comment.objects.filter(user="Sanaz Ferdosi fffff").exists()
    # queryset = Comment.objects.none()
    # queryset = Comment.objects.using("replica").filter(user="Sanaz Ferdosi")
    # queryset = Comment.objects.filter(user__startswith="ab")
    # queryset = Comment.objects.filter(user__endswith="mi")
    # queryset = Comment.objects.filter(user__contains="ab")
    # queryset = Comment.objects.filter(user__contains="mi")
    # queryset = Movie.objects.filter(rating__gt=9.0)
    # queryset = Movie.objects.filter(rating__gte=9.0)
    # queryset = Movie.objects.filter(rating__lt=9.0)
    # queryset = Movie.objects.filter(rating__lte=9.0)
    # queryset = Movie.objects.filter(rating__gt=6.0, rating__lt=9.0)
    # queryset = Movie.objects.filter(rating__range=[6.0, 9.0])
    # sensitive
    # insensitive
    # case-sesitive
    # case-insesitive
    # queryset = Comment.objects.filter(user__exact="Sanaz Ferdosi")
    # queryset = Comment.objects.filter(user__iexact="sanaz Ferdosi")
    # queryset = Comment.objects.filter(user__contains="sanaz")
    # queryset = Comment.objects.filter(user__icontains="sanaz")
    # queryset = Movie.objects.filter(status__in=["released", "post"])
    # queryset = Movie.objects.filter(title__regex=r'^[A-Z]')
    # queryset = Artist.objects.filter(birth_date=date(1966, 10, 19))
    # queryset = Artist.objects.filter(birth_date__year=1966)
    # queryset = Artist.objects.filter(birth_date__month=5)
    # queryset = Artist.objects.filter(birth_date__week_day=1)
    # queryset = Artist.objects.filter(birth_date__isnull=True)
    # queryset = Artist.objects.filter(birth_date__isnull=False)
    # queryset = Movie.objects.filter(year=(F("rating")*201.8))
    # queryset = Movie.objects.filter(status__in=["released", "post", "filming", "pre"])
    # queryset = Movie.objects.exclude(status__in=["develope"])
    # 1
    # queryset = GenreMovie.objects.all()
    # 2
    # queryset = Movie.objects.filter(status=Movie.STATUS_POST_PRODUCTION)
    # 3
    # queryset = Movie.objects.filter(title__icontains="avengers")
    # 4
    # queryset = Movie.objects.filter(genre__title="action")
    # 5
    # queryset = Artist.objects.filter(first_name__iexact="benedict")
    # 6
    # queryset = Artist.objects.filter(first_name__icontains="robert")
    # 7
    # queryset = Artist.objects.filter(birth_date__isnull=False)
    # 8
    # queryset = Movie.objects.filter(year__gte=2010)
    # 9
    # queryset = Comment.objects.filter(movie__title__icontains="avengers")
    # 10
    # queryset = Movie.objects.filter(year__in=[2003, 2005, 2007, 2009])
    # 11
    # queryset = Movie.objects.filter(year__in=[i for i in range(2003, 2026, 2)])
    # 12
    # queryset = Artist.objects.filter(birth_date__range=[date(1960, 1, 1), date(1970, 1, 1)])
    # queryset = Artist.objects.filter(birth_date__year__range=[1960, 1969])
    # 13
    # queryset = Movie.objects.filter(cast__first_name__icontains="robert")
    # 14
    # queryset = Movie.objects.filter(
    #     cast__first_name__iexact="benedict",
    #     cast__last_name__iexact="cumberbatch",
    #     rating__gte=9,
    # )
    # 15
    # queryset = Movie.objects.filter(cast__first_name__iexact="benedict")
    # 16
    # queryset = Movie.objects.filter(cast__first_name__iexact="benedict").distinct()
    # 17
    # queryset = Comment.objects.filter(
    #     movie__title__icontains="avengers",
    #     movie__year__range=(2018,2020),
    #     ).select_related("movie")
    # 18
    # queryset = (
    #     Comment.objects.filter(
    #         movie__title__icontains="avengers",
    #         movie__year__range=(2018, 2020),
    #     )
    #     .select_related("movie")
    #     .prefetch_related("movie__cast")
    # )
    # 19
    # queryset = Movie.objects.filter(comments__text__icontains="lorem").distinct()
    # 20
    # queryset = Artist.objects.filter(birth_date__isnull=False, nick_name__isnull=False)
    # queryset = Artist.objects.filter(Q(birth_date__isnull=False), ~Q(nick_name=""))
    # 21
    # queryset = Movie.objects.filter(Q(year__gte=2010) | Q(cast__first_name__icontains="robert")).distinct()
    # 22
    # queryset = Movie.objects.annotate(actor_count=Count("cast")).filter(actor_count=4)
    # 23
    # queryset = Movie.objects.annotate(actor_count=Count("cast")).filter(actor_count__lt=4)
    # 24
    # movies_with_at_least_5_cast = Movie.objects.annotate(
    #     actor_count=Count("cast")
    # ).filter(
    #     actor_count__gt=4,
    #     year__gte=2010,
    #     rating__gte=9,
    #     genre__title__iexact="action",
    # )
    # queryset = Comment.objects.filter(text__icontains="d", movie__in=movies_with_at_least_5_cast)
    # for item in queryset:
    #     print(item)
    # print(len(queryset))
    # context = {"queryset": queryset}
    # return render(request, "home.html", context)

def home(request):
    # comments = Comment.objects.all().select_related("movie")
    # comments = Comment.objects.filter(user__icontains="Kamran Babayi", movie__genre__title__iexact="action").select_related("movie")
    # context = {"comments": comments}
    # comments = Comment.objects.all().select_related("movie").prefetch_related("movie__cast")
    # comments = Comment.objects.filter(user__icontains="Kamran Babayi", movie__genre__title__iexact="action").select_related("movie").prefetch_related("movie__cast")
    # context = {"comments": comments}
    movies = Movie.objects.all().prefetch_related("comments", "genre", "cast")
    # movies = Movie.objects.all()
    context = {"movies": movies}

    return render(request, "home.html", context)

