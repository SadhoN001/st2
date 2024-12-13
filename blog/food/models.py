from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateField()
    completed = models.BooleanField(default=False)
    
class Service(models.Model):
    service_icon= models.CharField(max_length=50)
    service_title= models.CharField(max_length=50)
    service_des= models.TextField()