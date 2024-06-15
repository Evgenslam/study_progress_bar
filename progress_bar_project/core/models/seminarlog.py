from django.db import models

from ..base_model import BaseModel

# TODO: finish the model


class Seminar(BaseModel):
    """Онлайн занятие с учителем."""
    pass

    # class Status(models.TextChoices):
    #     NEW = "new", "Новый"
    #     INTEGRATING = "integrating", "На стадии интеграции"
    #     INTEGRATED = "integrated", "Интеграция окончена"

    # name = models.CharField("Название ресторана", unique=True)
    # status = models.CharField(
    #     "Статус интеграции",
    #     choices=Status.choices,
    #     default=Status.NEW,
    # )
    # description = models.TextField("Описание ресторана")
    # acceptTime_end = models.TimeField("Время окончания приёма заказов")
    # cuisines = models.ManyToManyField(
    #     "Cuisine",
    #     through="RestaurantCuisine",
    #     blank=True,
    # )

    # class Meta:
    #     verbose_name = "Ресторан"
    #     verbose_name_plural = "Рестораны"
    #     ordering = ("-created_at",)

    # def __str__(self):
    #     return self.name
