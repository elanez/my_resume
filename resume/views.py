from django.shortcuts import render
from resume.models import PersonalInformation, Skill, Education, Experience, Project

# Create your views here.

def index(request):
    personal_info = PersonalInformation.objects.first()
    # skills = Skill.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    context = {
        'personal_info': personal_info,
        # 'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
    }
    return render(request, 'resume/index.html', context)
