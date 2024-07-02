from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from .models import *
from .forms import LoginForm
from django.shortcuts import get_object_or_404, redirect # type: ignore

def home_page(request):
    return render(request,'pages/home.html')

def about_page(request):
    return render(request,'pages/about.html')

def contact_page(request):
    return render(request,'pages/contact.html')

def login_page(request):
    programs = Program.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Extract data from validated form
            full_name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            program_id = form.cleaned_data['program'].id
            course_id = form.cleaned_data['course'].id

            try:
                # Create a new Student instance
                student = Student.objects.create(
                    name=full_name,
                    age=age,
                    phone=phone,
                    email=email,
                    program_id=program_id  
                )

                # Create a new Enrollment instance
                enrollment = Enrollment.objects.create(
                    student=student,
                    course_id=course_id  
                )

                # Clear the form after successful submission
                form = LoginForm()

                # Redirect to CRUD page after successful submission
                return redirect('crud_page')

            except Exception as e:
                print(e) 
    else:
        form = LoginForm()

    return render(request, 'pages/loginform.html', {'form': form, 'programs': programs, 'courses': courses})

def crud_page(request):
    if request.method == 'POST':
        # Check if the form is for deleting a student
        if 'delete_student' in request.POST:
            student_id = request.POST.get('delete_student')
            student = get_object_or_404(Student, id=student_id)
            student.delete()
            return redirect('crud_page')

    students = Student.objects.prefetch_related('program').all()
    return render(request, 'pages/crud.html', {'students': students})



