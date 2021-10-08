from django.shortcuts import render
from django.db.models import QuerySet
from django.views import generic
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import viewsets 


class ReportView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer



class ArchiveListView(generics.ListAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer


class ArchiveCreateView(generics.CreateAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer    