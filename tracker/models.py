from datetime import timedelta

from django.db import models
from rest_framework.exceptions import ValidationError


class Habit(models.Model):
    owner = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец")
    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=100, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=True, verbose_name="Признак приятной привычки")
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Связанная привычка"
    )
    period = models.PositiveIntegerField(default=1, verbose_name="Число повторений в неделю")
    award = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вознаграждение")
    time_to_action = models.DurationField(default=timedelta(minutes=2), verbose_name="Время на выполнение")
    is_published = models.BooleanField(default=True, verbose_name="Признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.action}"

    def clean(self):
        if self.award and self.related_habit:
            raise ValidationError("Укажите вознаграждение или связанную привычку")
        if self.is_pleasant and (self.award or self.related_habit):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")
        if self.time_to_action > timedelta(seconds=120):
            raise ValidationError("Время выполнения должно быть не больше 120 секунд")
        if self.period > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней, и чаще, чем раз в день")
