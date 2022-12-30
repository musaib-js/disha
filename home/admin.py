from django.contrib import admin
from .models import Email, Contact, Video, Service, College, Courses

admin.site.register((Email, Contact, Video, Service, Courses, College))
