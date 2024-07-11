from django.contrib import admin
from .models import Teacher, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    search_fields = ('name', 'subject')
    list_filter = ('subject',)
    ordering = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'get_teachers')
    search_fields = ('name', 'group')
    list_filter = ('group',)
    ordering = ('name',)

    def get_teachers(self, obj):
        return ", ".join([teacher.name for teacher in obj.teachers.all()])

    get_teachers.short_description = 'Учителя'
