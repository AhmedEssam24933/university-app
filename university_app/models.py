from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=255, verbose_name="الاسم")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "كلية"
        verbose_name_plural = "الكليات"


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name="الاسم")
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name="الكلية")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "الأقسام"


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="الاسم")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="القسم")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "كورس"
        verbose_name_plural = "الكورسات"

class Prerequisit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="الكورس")
    prerequisites = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="المتطلبات", related_name='prerequisite_for')

    unique_together = ('course', 'prerequisites')
    def __str__(self):
        return f'{self.course.name} requires {self.prerequisites.name}'
    
    class Meta:
        verbose_name = "متطلب"
        verbose_name_plural = "المتطلبات"

class Student(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=255, verbose_name="الاسم الأخير")
    email = models.EmailField(null=True, blank=True, verbose_name="البريد الالكتروني")
    date_of_birth = models.DateField(verbose_name="تاريخ الميلاد")
    address = models.CharField(max_length=255, verbose_name="العنوان")
    city = models.CharField(max_length=255, verbose_name="المدينة")
    zip_code = models.CharField(max_length=10, verbose_name="الكود")
    phone_number = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    major = models.CharField(max_length=255, verbose_name="الأساسي")
    gpa = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="التقدير")
    graduation_date = models.DateField(verbose_name="تاريخ التخرج")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "طالب"
        verbose_name_plural = "الطلاب"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="الكورس")
    semester = models.CharField(max_length=10, verbose_name="الفصل الدراسي")
    grade = models.CharField(max_length=2, verbose_name="الدرجة")

    def __str__(self):
        return f"{self.student} enrolled in {self.course} during {self.semester}"
    
    class Meta:
        verbose_name = "تسجيل"
        verbose_name_plural = "التسجيلات"

