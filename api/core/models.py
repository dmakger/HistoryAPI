from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Type(models.Model):
    wallpaper = models.ImageField("Обложка", null=True, blank=True, default=None, upload_to="type/")
    title = models.CharField("Название", max_length=32, unique=True)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.title


class Person(models.Model):
    lastname = models.CharField("Фамилия", max_length=32, blank=True, null=True, default=None)
    username = models.CharField("Имя", max_length=32)
    pastname = models.CharField("Отчество", max_length=32, blank=True, null=True, default=None)
    description = RichTextUploadingField("Описание")
    image = models.ImageField("Аватар", null=True, blank=True, default=None, upload_to="person/")
    date_birth = models.DateField("Дата рождения")
    date_death = models.DateField("Дата смерти")

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"

    def __str__(self):
        return f"{self.lastname} {self.username} {self.pastname} ({self.date_birth} - {self.date_death})"


class Event(models.Model):
    title = models.CharField("Название", max_length=32, unique=True)
    description = models.CharField("Описание", max_length=256, blank=True, null=True)
    content = RichTextUploadingField("Контент")
    image = models.ImageField("Изображение", null=True, blank=True, default=None, upload_to="event/")
    types = models.ManyToManyField(to=Type, verbose_name="Типы")
    persons = models.ManyToManyField(to=Person, verbose_name="Персоны")

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return self.title
