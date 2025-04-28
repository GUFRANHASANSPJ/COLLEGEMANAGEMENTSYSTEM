# Project Description: College Management System
The College Management System is a Django-based web application that facilitates the management of various
<br>
 college activities, including student registration, faculty management, internship placements, events, and
<br>
more. The system provides a user-friendly interface for administrators, faculty, and students to manage their
<br>
 profiles, track academic progress, and stay updated with upcoming events and opportunities. Faculty members 
<br>
 can also manage student marks, daily reports, and placements, making it an all-in-one solution for college 
<br>
 administration.





##  Key Features

* <b> Student Registration</b> Students can register, update their profiles, and view their academic details.
* <b> Faculty Registration</b> Faculty members can register and manage their profiles, as well as monitor student progress.
* <b> Student Dashboard:</b>A personalized dashboard for students to view their marks, internship details, and daily status reports.
* <b> Faculty Dashboard:</b> A dashboard for faculty members to manage student marks, placements, and internships, as well as add events.
* <b> Placement Management:</b>  Faculty can add and manage placement opportunities for students.
* <b> Internship Management:</b> Students can view and update their internship details, while faculty can add
* <b>Event Management:</b> Faculty can create and manage events, and students can participate in them.
* <b> Daily Status Reports: </b> Students can submit daily progress reports, and faculty can monitor them.
* <b> Easy Navigation: </b> User-friendly interface for both students and faculty with simple forms and easy navigation.
* <b>Authentication & Authorization: </b> Role-based access control for students and faculty members.

## Technologies Used
* Backend: Django (Python)
* Frontend: HTML, CSS, JavaScript
* Database: MySQL (can be extended to PostgreSQL or SQLite)
* APIs: Django's internal APIs, 
* Third-Party Libraries: Django Forms, Django Pagination, and Email backend for notifications.
<hr>

## How to run this project


1. **Clone the project**

```sh
git clone https://github.com/GUFRANHASANSPJ/COLLEGEMANAGEMENTSYSTEM.git
```

2.  **Make sure you are in *RateMyNest* folder**


3. **Active virtual environment (env)**
```sh
    env\scripts\activate
```

4. **install requirements**
```sh
pip install -r requirements.txt
```

5. **Run Migrations**

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

```

6. **Run Server**

```sh
python manage.py runserver
```

7. **And Creating an admin user (superuser)**

```sh
python manage.py createsuperuser
```


<hr>
