import json
from django.shortcuts import redirect, get_object_or_404
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Department, Course, Faculty, Student, Enrollment
from .serializers import FacultySerializer, DepartmentSerializer, CourseSerializer, StudentSerializer, EnrollmentSerializer


@login_required
def home(request):
    return render(request, "registration/index.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return render(request, "registration/new_data.html")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def new_data(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        date_of_birth = request.POST['dateofbirth']
        address = request.POST['address']
        city = request.POST['city']
        zip_code = request.POST['zipcode']
        phone_number = request.POST['phonenumber']
        major = request.POST['major']
        gpa = request.POST['gpa']
        graduation_date = request.POST['graduationdate']
        student = Student(first_name=first_name, last_name=last_name, email=email, date_of_birth=date_of_birth, address=address,
        city=city,zip_code=zip_code, phone_number=phone_number, major=major, gpa=gpa, graduation_date= graduation_date)
        student.save()
        student = Student.objects.all()
        return render(request, 'registration/new_data.html', {'student':student})


# def return_json(obj, lst1):
#     data = obj.objects.all()
#     result = []
#     for k in data:
#         result_dict = {lst1[j]: getattr(k, lst1[j]) for j in range(len(lst1))}
#         print(result_dict)
#         result.append(result_dict)
#     json_result = json.dumps(result)
#     json_to_obj = json.loads(json_result)
#     return json_to_obj

# def faculty(request):
#     lst1 = ["id", "name"]
#     faculty2 = return_json(Faculty, lst1)
#     return render(request, 'registration/show_data.html', {'faculty2': faculty2})


# def student(request):
#     lst1 = ["id", "first_name", "last_name"]
#     student2 = return_json(Student, lst1)
#     return render(request, 'registration/students.html', {'student2': student2})

def data(obj):
    all_objects = obj.objects.all()
    return all_objects

def faculty(request):
    faculty2 = data(Faculty)
    return render(request, 'registration/show_data.html', {'faculty2': faculty2})

def student(request):
    student2 = data(Student)
    return render(request, 'registration/students.html', {'student2': student2})

def delete_data(request, id, class_name):
    if request.method == "POST":
        id = request.POST['pk']
        record = class_name.objects.get(id=id)
        record.delete()
    return request

def delete_faculty(request):
    request = delete_data(request, id, Faculty)
    return render(request, 'registration/delete_faculty.html')

# def delete_student(request):
#     if request.method == "POST":
#         id = request.POST['id']
#         record = Student.objects.get(id=id)
#         record.delete()
#     return redirect('/http://127.0.0.1:8000/student/')

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student')
    return redirect('student', pk=student.pk)

# def delete_faculty(request):
#     if request.method == "POST":
#         id = request.POST['pk']
#         record = Faculty.objects.get(id=id)
#         record.delete()
#     return render(request, 'registration/delete_faculty.html')

def get_students(request):
    all_students = Student.objects.all()
    for student in all_students:
        students = json.dumps({'id': student.id, 'first name': student.first_name})
    return render(request, 'registration/show_students.html', {'student':students})

def get_and_post(request, class_name, serializer_name):
    # GET
    if request.method == 'GET':
        obj = class_name.objects.all()
        serializer = serializer_name(obj, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = serializer_name(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def faculty_list(request):
    response = get_and_post(request, Faculty, FacultySerializer)
    return response

@api_view(['GET','POST'])
def department_list(request):
    response = get_and_post(request, Department, DepartmentSerializer)
    return response

@api_view(['GET','POST'])
def course_list(request):
    response = get_and_post(request, Course, CourseSerializer)
    return response

@api_view(['GET','POST'])
def students_list(request):
    response = get_and_post(request, Student, StudentSerializer)
    return response

@api_view(['GET','POST'])
def enrollment_list(request):
    response = get_and_post(request, Enrollment, EnrollmentSerializer)
    return response


def get_pk(request, pk, class_name, serializer_name):
    try:
        obj = class_name.objects.get(pk=pk)
    except class_name.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = serializer_name(obj)
        return Response(serializer.data)       
    # PUT
    elif request.method == 'PUT':
        serializer = serializer_name(obj, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        obj.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def faculty_pk(request, pk):
    response = get_pk(request, pk, Faculty, FacultySerializer)
    return response

@api_view(['GET','PUT','DELETE'])
def department_pk(request, pk):
    response = get_pk(request, pk, Department, DepartmentSerializer)
    return response

@api_view(['GET','PUT','DELETE'])
def course_pk(request, pk):
    response = get_pk(request, pk, Course, CourseSerializer)
    return response

@api_view(['GET','PUT','DELETE'])
def student_pk(request, pk):
    response = get_pk(request, pk, Student, StudentSerializer)
    return response

@api_view(['GET','PUT','DELETE'])
def enrollment_pk(request, pk):
    response = get_pk(request, pk, Enrollment, EnrollmentSerializer)
    return response 

