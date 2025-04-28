from django.shortcuts import render, redirect

from college.forms import EventForm, PlacementManagementForm 
from .forms import UserRegistrationForm, StudentProfileForm, FacultyProfileForm,InternshipForm,StudentMarkForm,StudentDailyStatusForm
from django.contrib.auth.models import User
from college.models import PlacementManagement,Event
from accounts.models import StudentProfile,FacultyProfile,Internship,StudentMark,StudentDailyStatus
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Student Registration
def student_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = StudentProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')  
    else:
        user_form = UserRegistrationForm()
        profile_form = StudentProfileForm()

    return render(request, 'accounts/student_reg.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

# Faculty Registration
def faculty_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = FacultyProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        profile_form = FacultyProfileForm()

    return render(request, 'accounts/faculty_reg.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def student_dashboard(request):
    try:
        student_profile = request.user.studentprofile

        student_marks = StudentMark.objects.filter(student=student_profile)
        daily_status = StudentDailyStatus.objects.filter(student=student_profile)
        internship_details = Internship.objects.filter(student=student_profile)

        events = Event.objects.all()
        placements = PlacementManagement.objects.all()

        context = {
            'student_profile': student_profile,
            'student_marks': student_marks,
            'daily_status': daily_status,
            'internship_details': internship_details,
            'events': events,
            'placements': placements,
        }

        return render(request, 'accounts/student_dashboard.html', context)

    except StudentProfile.DoesNotExist:
        return render(request, 'accounts/student_dashboard.html')  # Optional: show an error message

def edit_student_profile(request, id):
    student_profile = get_object_or_404(StudentProfile, id=id)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=student_profile)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')  
    else:
        form = StudentProfileForm(instance=student_profile)

    return render(request, 'accounts/edit_student_profile.html', {'form': form})

def edit_faculty_profile(request, faculty_id):  
    faculty_profile = get_object_or_404(FacultyProfile, id=faculty_id)  

    if request.method == 'POST':
        form = FacultyProfileForm(request.POST, request.FILES, instance=faculty_profile)
        if form.is_valid():
            form.save()
            return redirect('faculty_dashboard')  
    else:
        form = FacultyProfileForm(instance=faculty_profile)

    return render(request, 'accounts/edit_faculty_profile.html', {'form': form})

@login_required
def faculty_dashboard(request):
    faculty_profile = FacultyProfile.objects.get(user=request.user)
    event_form = EventForm()
    placement_form = PlacementManagementForm()
    daily_status_form = StudentDailyStatusForm()
    student_mark_form = StudentMarkForm()
    internship_form = InternshipForm()

    context = {
        'faculty_profile': faculty_profile,
        'daily_status_form': daily_status_form,
        'event_form': event_form,
        'student_mark_form': student_mark_form,
        'internship_form': internship_form,
        'placement_form': placement_form,
    }
    return render(request, 'accounts/faculty_dashboard.html', context)

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        print("form******************")
        if form.is_valid():
            form.save()
    return redirect('faculty_dashboard')  

@login_required
def add_placement(request):
    if request.method == 'POST':
        form = PlacementManagementForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('faculty_dashboard')  
@login_required
def add_daily_status(request):
    if request.method == 'POST':
        form = StudentDailyStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_dashboard')
    return redirect('faculty_dashboard')


@login_required
def add_student_mark(request):
    if request.method == 'POST':
        form = StudentMarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_dashboard')
    return redirect('faculty_dashboard')


@login_required
def add_internship(request):
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_dashboard')
    return redirect('faculty_dashboard')

# Add a method to the User model to check if the user is a Student or Faculty

def show_all_students(request):
    students = StudentProfile.objects.all()
    return render(request, 'accounts/show_all_students.html', {'students': students})

def show_all_company(request):
    companies = PlacementManagement.objects.all()
    return render(request, 'accounts/show_all_companies.html', {'companies': companies})

def view_student(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    
    internships = Internship.objects.filter(student=student)
    daily_status = StudentDailyStatus.objects.filter(student=student)
    events = Event.objects.filter(participants=student)
    marks = StudentMark.objects.filter(student=student)

    context = {
        'student': student,
        'internships': internships,
        'daily_status': daily_status,
        'events': events,
        'marks': marks,
    }
    return render(request, 'accounts/view_student_for_faculty.html', context)


def edit_student(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)

    internship = Internship.objects.filter(student=student).first()
    placement = PlacementManagement.objects.filter(participants=student).first()
    daily_status = StudentDailyStatus.objects.filter(student=student).first()
    student_marks = StudentMark.objects.filter(student=student)

    if request.method == 'POST':
        internship_form = InternshipForm(request.POST, instance=internship)
        placement_form = PlacementManagementForm(request.POST, instance=placement)
        daily_status_form = StudentDailyStatusForm(request.POST, instance=daily_status)

        # Save individually if valid
        if internship_form.is_valid():
            internship_form.save()

        if placement_form.is_valid():
            placement_form.save()

        if daily_status_form.is_valid():
            daily_status_form.save()

        # Saving each mark individually
        for mark in student_marks:
            mark_form = StudentMarkForm(request.POST, instance=mark, prefix=str(mark.id))
            if mark_form.is_valid():
                mark_form.save()

        return redirect('show_all_students')

    else:
        internship_form = InternshipForm(instance=internship)
        placement_form = PlacementManagementForm(instance=placement)
        daily_status_form = StudentDailyStatusForm(instance=daily_status)

    mark_forms = [StudentMarkForm(instance=mark, prefix=str(mark.id)) for mark in student_marks]

    context = {
        'internship_form': internship_form,
        'placement_form': placement_form,
        'daily_status_form': daily_status_form,
        'mark_forms': mark_forms,
        'student': student,
    }
    return render(request, 'accounts/edit_student_details_for_faculty.html', context)

def delete_company(request, id):
    company = get_object_or_404(PlacementManagement, id=id)
    company.delete()
    return redirect('show_all_companies') 

def edit_company(request, id):
    company = get_object_or_404(PlacementManagement, id=id)

    if request.method == 'POST':
        form = PlacementManagementForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('show_all_companies')  
    else:
        form = PlacementManagementForm(instance=company)

    return render(request, 'accounts/show_all_companies.html', {'companies': PlacementManagement.objects.all()})


def is_student(self):
    return hasattr(self, 'studentprofile')

def is_faculty(self):
    return hasattr(self, 'facultyprofile')

User.add_to_class('is_student', is_student)
User.add_to_class('is_faculty', is_faculty)