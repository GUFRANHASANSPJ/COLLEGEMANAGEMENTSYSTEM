from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=50,null=True, blank=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    course = models.CharField(max_length=100,null=True, blank=True)
    enrollment_number = models.CharField(max_length=20, unique=True)
    image= models.ImageField(upload_to='student',null=True, blank=True)

    def __str__(self):
        return self.full_name

class StudentDailyStatus(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Conducting Event', 'Conducting Event'),
        ('Organizing Seminar/Workshop', 'Organizing Seminar/Workshop')
    ])

    def __str__(self):
        return f"{self.student.full_name} - {self.status} on {self.date}"

class StudentMark(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,null=True, blank=True)
    marks = models.CharField(max_length=5,null=True, blank=True)

class Internship(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,null=True, blank=True)
    duration = models.CharField(max_length=50,null=True, blank=True)
    

class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=50,null=True, blank=True)
    phone = models.CharField(max_length=15)
    professional_details = models.CharField(max_length=100, null=True, blank=True)
    image= models.ImageField(upload_to='faculty',null=True, blank=True)

    def __str__(self):
        return self.full_name

