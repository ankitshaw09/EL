from rest_framework import serializers
from .models import LiveClass

class LiveClassSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source="course.name", read_only=True)
    instructor_name = serializers.CharField(source="instructor.full_name", read_only=True)
    is_live = serializers.SerializerMethodField()

    class Meta:
        model = LiveClass
        fields = ["id", "course_name", "instructor_name", "start_time", "end_time", "meeting_link", "is_live"]

    def get_is_live(self, obj):
        return obj.is_live()
