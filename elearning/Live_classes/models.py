from django.db import models
from authentication.models import CustomUser
from courses.models import Course
from django.utils.timezone import now

class LiveClass(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="live_classes")
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="hosted_live_classes")
    start_time = models.DateTimeField()  # Start time of the class
    end_time = models.DateTimeField()  # End time of the class
    meeting_link = models.URLField()  # Link to join the class

    def is_live(self):
        """Check if the class is currently live."""
        return self.start_time <= now() <= self.end_time

    def __str__(self):
        return f"{self.course.name} - Live Class"
