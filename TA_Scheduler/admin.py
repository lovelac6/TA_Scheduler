from django.contrib import admin
from TA_Scheduler.models import User, Course, CourseAssignment

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(CourseAssignment)

