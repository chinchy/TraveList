from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Object(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name="Название", max_length=128)
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    image = models.ImageField(verbose_name="Изображение")
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE)
