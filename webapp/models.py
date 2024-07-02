from django.db import models # type: ignore

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)  
    email = models.EmailField(max_length=50, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='students', blank=True, null=True)

    @property
    def enrolled_course(self):
        try:
            enrollment = self.enrollments.first()
            if enrollment:
                return enrollment.course
        except Enrollment.DoesNotExist:
            pass
        return None

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    courses_taught = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='teachers_taught', blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='courses')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses_taught_by_teacher')

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"
