from django.db import models
from accounts.models import StudentProfile


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100,null=True, blank=True)
    date = models.DateField()

    participants = models.ManyToManyField(StudentProfile, blank=True, related_name='joined_events')

    def __str__(self):
        return self.title
    
class PlacementManagement(models.Model):
    company_name = models.CharField(max_length=100,null=True, blank=True)
    job_role = models.CharField(max_length=100,null=True, blank=True)
    package = models.CharField(max_length=50,null=True, blank=True)
    skills_required= models.CharField(max_length=100,null=True, blank=True)
    participants = models.ManyToManyField(StudentProfile, blank=True, related_name='applied_student')
    date_applied = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.participants} - {self.company_name} "