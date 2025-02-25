from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from .models import LiveClass
from .serializers import LiveClassSerializer

class CurrentLiveClassesView(ListAPIView):
    serializer_class = LiveClassSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Get live classes for the logged-in user."""
        user_id = self.kwargs["userId"]
        return LiveClass.objects.filter(course__enrolled_users__id=user_id, start_time__lte=now(), end_time__gte=now())
