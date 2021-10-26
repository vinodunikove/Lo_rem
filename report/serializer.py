from rest_framework import serializers
from .models import DailyFieldReports

class  DailyFieldReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model= DailyFieldReports
        fields='__all__'


