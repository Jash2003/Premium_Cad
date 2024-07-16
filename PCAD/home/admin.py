from django.contrib import admin

# Register your models here.
from .models import Blog,Applicant

admin.site.register(Blog)
admin.site.register(Applicant)