from django.db import models
from datetime import date


class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=50, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=50, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField(verbose_name="Изображение")

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.category}'


class Movie(models.Model):
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2024)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры", related_name="film_genres")
    director = models.ManyToManyField(Director, verbose_name="режиссёр",)
    world_premiere = models.DateField("Примьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text="указывать сумму в долларах")
    fess_in_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text="указывать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, null=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title


class MovieShots(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='ing/', null=True, blank=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Good(models.Model):
    CHOISEC_STAR = (
        ("5", "5"),
        ("4", "4"),
        ("3", "3"),
        ("2", "2"),
        ("1", "1")
    )
    star = models.CharField(max_length=16, choices=CHOISEC_STAR)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм")


class Comment(models.Model):
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.movie}"


