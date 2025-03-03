from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ["id", "title", "video_file", "uploaded_at"]  

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "file"]

class CourseSerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(many=True, read_only=True)  
    notes = NoteSerializer(many=True, read_only=True)  

    class Meta:
        model = Course
        fields = [
            "id", "name", "description", "creator_name", "rating",
            "level", "duration_weeks", "total_lectures", "price", 
            "discount_percentage", "discounted_price", "lectures", "notes"
        ]

class UserCourseProgressSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = UserCourseProgress
        fields = ['course', 'status', 'progress_percentage']

class EnrollCourseSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()
    confirm = serializers.BooleanField()

    def validate(self, data):
        """Check if confirmation is provided"""
        if not data.get("confirm"):
            raise serializers.ValidationError("Please confirm enrollment.")
        return data


class LearningTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningTip
        fields = ['id', 'title', 'description']
