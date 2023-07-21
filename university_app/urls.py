from .views import student,delete_student, home,new_data, department_list, department_pk, course_list, course_pk, faculty_list, faculty_pk, students_list, student_pk, enrollment_list, enrollment_pk, register, faculty, delete_faculty, get_students
from django.contrib.auth import views as auth_views
from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('home/', home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('home/new_data/', new_data, name='new_data'),
    path('faculty/', faculty, name='faculty'),
    path('student/', student, name='student'),
    path('student/<int:pk>/delete/', delete_student, name='delete_student'),
    path('faculty/delete_faculty/', delete_faculty, name='delete_faculty'),
    path('get_students/', get_students, name='get_students'),
    path('department_list/', department_list, name='department_list'),
    path('department_pk/<int:pk>/', department_pk, name='department_pk'),
    path('course_list/', course_list, name='course_list'),
    path('course_pk/<int:pk>/', course_pk, name='course_pk'),
    path('faculty_list/', faculty_list, name='faculty_list'),
    path('faculty_pk/<int:pk>/', faculty_pk, name='faculty_pk'),
    path('students_list/', students_list, name='students_list'),
    path('student_pk/<int:pk>/', student_pk, name='student_pk'),
    path('enrollment_list/', enrollment_list, name='enrollment_list'),
    path('enrollment_pk/<int:pk>/', enrollment_pk, name='enrollment_pk'),
    #rest auth url
    path('api-auth', include('rest_framework.urls')),
    #Token Authentication
    # path('api-token-auth', obtain_auth_token)
]