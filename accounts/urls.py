from django.contrib import admin
from django.urls import path
from accounts import views 


urlpatterns = [
    path('accounts/admin/', admin.site.urls),
    path('studentreg/',views.student_register,name='studentreg'),
    path('facultyreg/',views.faculty_register,name='facultyreg'),
    path('login/',views.user_login,name='login' ),
    path('student_dashboard/',views.student_dashboard,name='student_dashboard' ),
    path('faculty_view/',views.faculty_dashboard,name='faculty_dashboard' ),
    path('add-event/', views.add_event, name='add_event'),
    path('add-placement/', views.add_placement, name='add_placement'),
    path('add_daily_status/', views.add_daily_status, name='add_daily_status'),
    path('add_student_mark/', views.add_student_mark, name='add_student_mark'),
    path('add_internship/', views.add_internship, name='add_internship'),
    path('students/', views.show_all_students, name='show_all_students'),
    path('companies/', views.show_all_company, name='show_all_companies'),
    path('students/<int:student_id>/', views.view_student, name='view_student'),
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('edit-profile/<int:id>/', views.edit_student_profile, name='edit_student_profile'),
    path('faculty/<int:faculty_id>/edit/', views.edit_faculty_profile, name='edit_faculty_profile'),

    path('company/edit/<int:id>/', views.edit_company, name='edit_company'),
    path('company/delete/<int:id>/', views.delete_company, name='delete_company'),

    path('logout/',views.user_logout,name='logout' ),
]
