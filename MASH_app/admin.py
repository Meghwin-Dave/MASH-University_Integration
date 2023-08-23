from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'HOD/ADMIN PANEL'
admin.site.register(Contactd)
admin.site.register(Newsletter)
admin.site.register(User)
admin.site.register(Master)
admin.site.register(Role)
admin.site.register(Assign)
admin.site.register(Faculty)
admin.site.register(Video)
admin.site.register(Note)
admin.site.register(Feedback)

