from .views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('ReportList/' ,  ReportView.as_view({'get':'list',})),
    path('ReportCreate/' ,  ReportView.as_view({'post':'create',})),
    path('ReportUpdate//<int:pk>/' ,  ReportView.as_view({'put':'retrieve',})),
    path('ReportDelete/<int:pk>/' ,  ReportView.as_view({'delete': 'destroy',})),

    path('ArchiveList/' ,  ArchiveListView.as_view()),
    path('ArchiveCreate/' ,   ArchiveCreateView.as_view()),

    path('ParameterCreate/' , ParameterCreateView.as_view()),
    path('ParameterList/' , ParameterListView.as_view())

]