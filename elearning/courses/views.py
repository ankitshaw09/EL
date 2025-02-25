import random
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


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
