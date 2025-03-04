from django.contrib import admin

from .models import PersonalInformation, Skill, Education, Experience, Project

# Register your models here.

admin.site.register(PersonalInformation)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)