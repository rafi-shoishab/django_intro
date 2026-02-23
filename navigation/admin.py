from django.contrib import admin
from .models import Students

# Register your models here.

# admin.site.register(Students)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'std_id', 'age', 'email', 'dob', 'dept')
    search_fields = ('name', 'std_id', 'email')
    list_filter = ('dept',)
    ordering = ('id',)