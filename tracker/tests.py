from datetime import datetime, timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tracker.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        """Функция подготовки данных перед тестированием"""
        self.user = User.objects.create(email="admin@example.com")
        self.user.set_password("0147")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            place="тест",
            time="07:00:00",
            action="тест",
            is_pleasant=False,
            period=1,
            award="тестовое вознаграждение",
            time_to_action=timedelta(seconds=60),
        )

    def test_habit_create(self):
        """Тестирование создания экземпляра привычки"""
        url = reverse("tracker:habit-create")
        data = {
            "place": "test",
            "time": "05:00:00",
            "action": "test",
            "period": 1,
            "time_to_action": timedelta(seconds=60),
        }
        response = self.client.post(url, data)
        print(datetime.now())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list(self):
        """Тестирование запроса на вывод списка привычек"""
        url = reverse("tracker:habit-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_habit_retrieve(self):
        """Тестирование запроса на вывод полей привычки по заданному pk"""
        url = reverse("tracker:habit-retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_update(self):
        """Тестирование запроса на изменение полей привычки"""
        url = reverse("tracker:habit-update", args=(self.habit.pk,))
        data_update = {
            "place": "тест",
            "action": "тест",
            "is_pleasant": False,
            "period": 1,
            "award": "тестовое вознаграждение",
            "time": "05:05:00",
            "time_to_action": timedelta(seconds=65),
        }
        response = self.client.patch(url, data=data_update)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("time"), "05:05:00")

    def test_habit_delete(self):
        """Тестирование запроса на удаление привычки с заданным pk"""
        url = reverse("tracker:habit-delete", kwargs={"pk": self.habit.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
