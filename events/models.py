from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Event(models.Model):
    college_name = models.CharField(max_length=100)
    college_code = models.CharField(max_length=10)
    event_details = models.TextField()
    event_image = models.ImageField(upload_to='event_images/')
    college_address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_details


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_college = models.CharField(max_length=100)
    student_email = models.EmailField()
    number_of_participants = models.IntegerField()
    participants_emails = models.TextField()  # Comma-separated emails

    def __str__(self):
        return f"{self.student_name} - {self.event.event_details}"