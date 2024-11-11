from django.contrib import admin
from .models import*
admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Subject)


class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']
admin.site.register(SubjectMark ,SubjectMarkAdmin )

# Register your models here.
