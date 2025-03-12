from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_by', 'created_at')
    search_fields = ('question', 'answer')


from django.contrib import admin
from .models import SupportTicket

class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('subject', 'description', 'user__username')
    ordering = ('-created_at',)
    readonly_fields = ('user', 'subject', 'description', 'created_at', 'updated_at')

    # Allow admins to update ticket status and response
    fields = ('user', 'subject', 'description', 'status', 'admin_response', 'created_at', 'updated_at')

admin.site.register(SupportTicket, SupportTicketAdmin)


from django.contrib import admin
from .models import HelpResource

@admin.register(HelpResource)
class HelpResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)


from django.contrib import admin
from .models import BugReport

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
