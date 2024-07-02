from django.contrib import admin # type: ignore
from .models import Program, Student, Teacher, Course, Enrollment

class EnrollmentInline(admin.StackedInline):
    model = Enrollment
    extra = 0

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'phone', 'email', 'program', 'enrolled_course_name')
    search_fields = ('name', 'email')
    inlines = [EnrollmentInline]

    def enrolled_course_name(self, obj):
        return obj.enrolled_course.name if obj.enrolled_course else '-'

    enrolled_course_name.short_description = 'Enrolled Course'

admin.site.register(Program)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Course)
