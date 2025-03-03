from django.contrib import admin
from .models import Course, Lecture, Note, Category

class LectureInline(admin.TabularInline):
    model = Lecture
    extra = 1  # Allows adding multiple videos at once

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1  # Allows adding multiple notes at once

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "creator_name", "category", "rating", "level", "price", "discounted_price")
    list_filter = ("category", "level")
    search_fields = ("name", "creator_name")
    inlines = [LectureInline, NoteInline]  # Add multiple videos & notes

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "uploaded_at")

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "uploaded_at")


from django.contrib import admin
from .models import LearningTip

@admin.register(LearningTip)
class LearningTipAdmin(admin.ModelAdmin):
    list_display = ("id", "title")  # Show ID and title in the admin list view
    search_fields = ("title", "description")  # Enable search by title & description
