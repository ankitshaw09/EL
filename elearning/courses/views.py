import random
from .models import *
from .serializers import *
from rest_framework import status
from authentication.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

class CategoryListView(APIView):
    """Retrieve a list of all course categories"""

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CourseListView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        limit = self.request.query_params.get("limit", 10)  # Default limit: 10
        try:
            limit = int(limit)
        except ValueError:
            limit = 10  # Fallback to default if invalid
        courses = list(Course.objects.all())  # Convert queryset to a list
        random.shuffle(courses)  # Shuffle courses randomly
        return courses[:limit]  # Return limited random courses


class EnrollCourseView(APIView):
    """API for enrolling a user in a course"""
    permission_classes = [IsAuthenticated]  # Only authenticated users

    def post(self, request):
        serializer = EnrollCourseSerializer(data=request.data)
        if serializer.is_valid():
            course_id = serializer.validated_data['course_id']
            user = request.user  # Authenticated user

            # Get course
            course = get_object_or_404(Course, id=course_id)

            # Check if already enrolled
            if course.enrolled_users.filter(id=user.id).exists():
                return Response({"message": "You are already enrolled in this course."}, status=status.HTTP_400_BAD_REQUEST)

            # Enroll user
            course.enrolled_users.add(user)

            # Create a progress record with 0% completed
            UserCourseProgress.objects.create(user=user, course=course)

            return Response({"message": f"Successfully enrolled in {course.name}."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LearningPathView(APIView):
    def get(self, request, userId):
        user = CustomUser.objects.get(id=userId)

        # Get all courses the user has enrolled in
        enrolled_courses = user.enrolled_courses.all()
        progress_records = UserCourseProgress.objects.filter(user=user)
        completed = []
        in_progress = []

        for course in enrolled_courses:
            # Check if user has progress recorded for this course
            progress = progress_records.filter(course=course).first()
            
            if progress:
                progress_data = {
                    "course": CourseSerializer(course).data,
                    "progress_percentage": progress.progress_percentage
                }
                if progress.progress_percentage == 100:
                    completed.append(progress_data)
                else:
                    in_progress.append(progress_data)
            else:
                # If user enrolled but hasn't started, show 0% progress
                in_progress.append({
                    "course": CourseSerializer(course).data,
                    "progress_percentage": 0.0
                })

        # Upcoming courses logic (can be customized) problem hai yaha pe 
        upcoming = Course.objects.exclude(id__in=enrolled_courses.values_list("id", flat=True))

        return Response({
            "in_progress": in_progress,
            "completed": completed,
            "upcoming": CourseSerializer(upcoming, many=True).data
        }, status=status.HTTP_200_OK)


class LearningTipsView(APIView):
    """API to retrieve general learning tips"""

    def get(self, request):
        tips = LearningTip.objects.all()
        serializer = LearningTipSerializer(tips, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


