from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home-page"),
    path("work-experience/<int:pk>", views.work_experience, name="work-experience"),
    path("education/<int:pk>", views.education, name="education"),
]