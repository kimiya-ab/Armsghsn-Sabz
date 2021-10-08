from .views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('ReportList/' ,  ReportView.as_view({'get':'list',})),
    path('ReportCreate/' ,  ReportView.as_view({'get':'create',})),
    path('ReportDelete//<int:pk>/' ,  ReportView.as_view({'get':'destory',})),
    path('ReportUpdate//<int:pk>/' ,  ReportView.as_view({'get':'retrieve',})),


    path('ArchiveList/' ,  ArchiveListView.as_view()),
    path('ArchiveCreate/' ,   ArchiveCreateView.as_view()),

]