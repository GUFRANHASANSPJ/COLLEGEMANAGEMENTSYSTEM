from django.contrib import admin
from.models import FacultyProfile,Internship,StudentMark,StudentDailyStatus,StudentProfile
# Register your models here.
from college.models import Event, PlacementManagement

admin.site.register(StudentProfile)
admin.site.register(StudentDailyStatus)
admin.site.register(StudentMark)
admin.site.register(Internship)
admin.site.register(FacultyProfile)
admin.site.register(Event)
admin.site.register(PlacementManagement)