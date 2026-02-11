from django.contrib import admin

from tracker.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("id", "action", "is_pleasant", "owner", "is_published")
    list_filter = ("action", "is_pleasant", "owner")
    search_fields = ("action", "is_pleasant", "owner")
