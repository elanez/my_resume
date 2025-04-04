from django.contrib import admin

from .models import PersonalInformation, Skill, Education, Experience, Project

# Register your models here.

admin.site.register(PersonalInformation)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_ongoing')
    list_filter = ('is_ongoing', 'start_date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, ProjectAdmin)