
from .models import StudentDailyStatus, StudentMark, Internship,StudentProfile,FacultyProfile
from django import forms
from college.models import PlacementManagement,Event
from django.contrib.auth.models import User



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'address', 'phone', 'date_of_birth', 'course', 'enrollment_number', 'image']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        fields = ['full_name', 'address', 'phone', 'professional_details', 'image']


class StudentDailyStatusForm(forms.ModelForm):
    class Meta:
        model = StudentDailyStatus
        fields = ['student', 'status']

class StudentMarkForm(forms.ModelForm):
    class Meta:
        model = StudentMark
        fields = ['student', 'subject', 'marks']

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ['student', 'company_name', 'duration']


class PlacementManagementForm(forms.ModelForm):
    class Meta:
        model = PlacementManagement
        fields = '__all__'

