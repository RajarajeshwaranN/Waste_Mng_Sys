from django.db import models
from django.contrib.auth.models import User
from model_utils import FieldTracker



class booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    address = models.TextField()
    waste_type = models.CharField(max_length=10)
    quantity = models.IntegerField()
    
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'booking'  # Use the existing `booking` table

    def __str__(self):
        return f"{self.user.name} - {self.date} at {self.time}"
    
class AdminTask(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Assigned', 'Assigned'),
        # ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    id = models.AutoField(primary_key=True)  
    request = models.ForeignKey(booking, on_delete=models.CASCADE, related_name='admin_tasks')
    assigned_admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    notes = models.TextField(blank=True, null=True)

    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='worker_tasks')  # The worker/collector assigned to the task

    assigned_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tracker = FieldTracker(fields=['status'])


    def __str__(self):
        return f"Task for {self.request} - {self.status}"

