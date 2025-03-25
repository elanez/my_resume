from django.shortcuts import render, get_object_or_404
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


def work_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    context = {
        'experience': experience,
    }
    return render(request, 'resume/experience.html', context)

def education(request, pk):
    education = get_object_or_404(Education, pk=pk)
    projects = education.projects.all()
    context = {
        'education': education,
        'projects': projects,
    }
    return render(request, 'resume/education.html', context)
