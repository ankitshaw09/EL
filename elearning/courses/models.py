from decimal import Decimal
from django.db import models
from authentication.models import CustomUser

class Category(models.Model):
    """Category for grouping courses"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=255)  # Course name
    description = models.TextField()  # Course description
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Course category
    
    creator_name = models.CharField(max_length=255)  # Course creator name
    creator_description = models.TextField()  # Creator's bio
    
    rating = models.FloatField(default=0.0)  # Course rating (out of 5)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)  # Course level
    duration_weeks = models.IntegerField()  # Duration in weeks

    certificate = models.FileField(upload_to="courses/certificates/", null=True, blank=True)  # Certificate

    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Course price
    discount_percentage = models.FloatField(default=0.0)  # Discount percentage
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Auto-calculated  

    # Enrollment
    enrolled_users = models.ManyToManyField(CustomUser, blank=True, related_name="enrolled_courses")  # Users who enrolled

    created_at = models.DateTimeField(auto_now_add=True)  # Course creation time  
    updated_at = models.DateTimeField(auto_now=True)  # Last updated time  

    def save(self, *args, **kwargs):
        """Automatically calculate discounted price before saving"""
        if self.discount_percentage > 0:
            discount_amount = (self.price * Decimal(self.discount_percentage)) / Decimal(100)
            self.discounted_price = self.price - discount_amount
        else:
            self.discounted_price = self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    @property
    def total_lectures(self):
        """Calculate total lectures dynamically (videos + notes)"""
        return self.lectures.count() + self.notes.count()

class Lecture(models.Model):
    """Stores multiple video lectures for a course"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lectures")
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to="courses/videos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.name} - {self.title}"

class Note(models.Model):
    """Stores multiple notes for a course"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="courses/notes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.name} - {self.title}"
    

class UserCourseProgress(models.Model):
    """Tracks user progress for enrolled courses"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    watched_lectures = models.ManyToManyField(Lecture, blank=True)  # Track watched lectures
    status = models.CharField(
        max_length=20, 
        choices=[('in_progress', 'In Progress'), ('completed', 'Completed')],
        default='in_progress'
    )

    @property
    def progress_percentage(self):
        """Calculate the progress percentage based on watched lectures."""
        total_lectures = self.course.lectures.count() 
        watched_count = self.watched_lectures.count()
        if total_lectures == 0:
            return 0
        return round((watched_count / total_lectures) * 100, 2)  # Round to 2 decimal places


    def __str__(self):
        return f"{self.user.full_name} - {self.course.name} ({self.status})"

class LearningTip(models.Model):
    """Model to store general learning tips"""
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
