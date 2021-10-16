from django.db import models
from User.models import Profile



class Report(models.Model):
    title = models.CharField(max_length=100)
    subtitlr = models.CharField(max_length=300)
    content = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField()



class Archive(models.Model):
    name = models.ForeignKey(Profile , default=None, null=True, on_delete=models.CASCADE)
    time = models.DateTimeField()
    date = models.DateField(auto_now_add=True)
    STATUSE_CHOICE = (
        ('saturday','SATURDAY'),
        ('sunday','SUNDAY'),
        ('monday','Mondaye'),
        ('tuesday','THUESDAYE'),
        ('wednesday', 'WEDNSEDAY'),
        ('thursday', 'THURSDAY'),
        ('friday' , 'FRIDAY'),
    )
    status = models.CharField(max_length=10,choices=STATUSE_CHOICE)
