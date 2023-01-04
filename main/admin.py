from django.contrib import admin
from .models import Task, Team, invitations

# Register your models here.

admin.site.register(Task)
admin.site.register(Team)
admin.site.register(invitations)



