from rest_framework.serializers import ModelSerializer

from tracker.models import Habit


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ["id", "owner"]

    def validate(self, attrs):
        habit = Habit(**attrs)
        habit.clean()
        return attrs
