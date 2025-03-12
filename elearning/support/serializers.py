from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'  # Return all fields


from rest_framework import serializers
from .models import SupportTicket

class SupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = ['id', 'user', 'subject', 'description', 'status', 'created_at', 'updated_at', 'admin_response']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'admin_response']


from rest_framework import serializers
from .models import HelpResource

class HelpResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpResource
        fields = '__all__'


from rest_framework import serializers
from .models import BugReport

class BugReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BugReport
        fields = '__all__'
