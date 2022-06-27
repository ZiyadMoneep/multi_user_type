from django.contrib import admin
from .models import User, Applicant, Recruiter, Supervisor, Secretary

# Register your models here.

admin.site.register(User)
admin.site.register(Applicant)
admin.site.register(Recruiter)
admin.site.register(Supervisor)
admin.site.register(Secretary)

