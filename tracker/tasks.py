from datetime import datetime, timedelta, date

from celery import shared_task

from tracker.models import Habit
from tracker.services import send_telegram_message


@shared_task
def task():
    """Периодическая задача, которая отправляет уведомления в телеграмм за 5 минут до начала выполнения привычки"""
    habits = Habit.objects.all()
    for habit in habits:
        t = datetime.combine(date.today(), habit.time) - timedelta(minutes=5)
        print(t.time() <= datetime.now().time())
        if habit.owner.chat_id and t.time() <= datetime.now().time():
            text = f"Я буду {habit.action} в {habit.time} в {habit.place}"
            send_telegram_message(text, habit.owner.chat_id)
