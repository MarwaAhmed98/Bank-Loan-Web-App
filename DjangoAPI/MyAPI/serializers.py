from rest_framework import serializers
from .models import approvals

class approvalsSerializer(serializers.ModelSerializer):
    class Meta:
        model= approvals
        fields= '__all__'
        