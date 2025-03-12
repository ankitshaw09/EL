from django.urls import path
from .views import *

urlpatterns = [
    path('faq/', FAQView.as_view(), name="get_faqs"),
    
    path('ticket/', CreateTicketView.as_view(), name='create-ticket'),  # User creates a ticket
    path('ticket/<int:ticket_id>/', TicketDetailView.as_view(), name='ticket-detail'),  # User fetches ticket details
    path('ticket/<int:ticket_id>/resolve/', ResolveTicketView.as_view(), name='resolve-ticket'),  # Admin resolves ticket
    
    
    path('resources/', HelpResourceView.as_view(), name='help-resources'),
    
    path('report-bug/', SubmitBugReportView.as_view(), name='submit-bug'),
    path('admin/help/bug-reports/', AdminBugReportView.as_view(), name='admin-bug-reports'),




]
