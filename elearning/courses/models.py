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
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Auto-calculated hai 

    # Enrollment
    enrolled_users = models.ManyToManyField(CustomUser, blank=True, related_name="enrolled_courses")  # Users who enrolled

    created_at = models.DateTimeField(auto_now_add=True)  # Course creation time  optional hai 
    updated_at = models.DateTimeField(auto_now=True)  # Last updated time  yeh bhi optional hai 

    def save(self, *args, **kwargs):
        # Automatically calculate discounted price before saving
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
        # Calculate total lectures dynamically (videos + notes
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
    # Stores multiple notes for a course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="courses/notes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.name} - {self.title}"