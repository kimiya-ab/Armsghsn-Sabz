from rest_framework import serializers
from django.db.models import fields
from .models import *


class ReportSerializer(serializers.ModelSerializer):
     class Meta:
        fields = '__all__'
        model = Report


class ArchiveSerializer(serializers.ModelSerializer):
     class Meta:
        fields = '__all__'
        model = Archive        



class ParameterSerializer(serializers.ModelSerializer):
   class Meta:
      fields = '__all__'
      model = Parameter