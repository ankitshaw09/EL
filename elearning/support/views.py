from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import FAQ
from .serializers import FAQSerializer

class FAQView(APIView):
    permission_classes = [AllowAny]  # Anyone can view FAQs

    def get(self, request):
        faqs = FAQ.objects.all().order_by('-created_at')  # Get all FAQs, newest first
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data, status=200)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .models import SupportTicket
from .serializers import SupportTicketSerializer

# ✅ User can create a support ticket
class CreateTicketView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SupportTicketSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(user=request.user)  # Assign the ticket to the logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ User can view their ticket details
class TicketDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, ticket_id):
        try:
            ticket = SupportTicket.objects.get(id=ticket_id, user=request.user)  # Ensure user can only see their ticket
            serializer = SupportTicketSerializer(ticket)
            return Response(serializer.data)
        except SupportTicket.DoesNotExist:
            return Response({"error": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND)

# ✅ Admin/Manager can update ticket status
class ResolveTicketView(APIView):
    permission_classes = [IsAdminUser]  # Only Admins/Managers can resolve tickets

    def put(self, request, ticket_id):
        try:
            ticket = SupportTicket.objects.get(id=ticket_id)
            status_update = request.data.get("status")
            admin_response = request.data.get("admin_response")

            if status_update:
                ticket.status = status_update  # Update ticket status

            if admin_response:
                ticket.admin_response = admin_response  # Admin's response

            ticket.save()
            return Response({"message": "Ticket updated successfully"})
        except SupportTicket.DoesNotExist:
            return Response({"error": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import HelpResource
from .serializers import HelpResourceSerializer

class HelpResourceView(APIView):
    """Fetch help resources like videos, PDFs, and articles."""
    permission_classes = [AllowAny]

    def get(self, request):
        resources = HelpResource.objects.all().order_by('-created_at')
        serializer = HelpResourceSerializer(resources, many=True)
        return Response(serializer.data, status=200)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import BugReport
from .serializers import BugReportSerializer

# 🚀 User submits a bug report
class SubmitBugReportView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data["user"] = request.user.id  # Auto-assign user
        serializer = BugReportSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Bug report submitted successfully!"}, status=201)
        
        return Response(serializer.errors, status=400)

# 🚀 Admin views all bug reports
class AdminBugReportView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        bug_reports = BugReport.objects.all().order_by('-created_at')
        serializer = BugReportSerializer(bug_reports, many=True)
        return Response(serializer.data, status=200)
