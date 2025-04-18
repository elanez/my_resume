from django.db import models

def profile_picture_upload_path(instance, filename):
    # Creates path like: uploads/profile_pictures/filename
    return f'uploads/profile_pictures/{filename}'

# Create your models here.

class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    summary = models.TextField()
    profile_picture = models.ImageField(upload_to=profile_picture_upload_path, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = "Personal Information"


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    gwa = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.degree}'
    
    class Meta:
        ordering = ['-end_date', '-start_date']
        verbose_name_plural = "Education"


class Experience(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    responsibilities = models.JSONField(default=list)
    skills = models.ManyToManyField(Skill, related_name='experiences')

    def __str__(self):
        return f'{self.title} at {self.company}'
    
    class Meta:
        ordering = ['-end_date', '-start_date']


def project_upload_path(instance, filename):
    # Creates path like: uploads/projects/filename
    return f'uploads/projects/{filename}'

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_description = models.CharField(max_length=100)
    detailed_description = models.TextField()
    image = models.ImageField(upload_to=project_upload_path, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_ongoing = models.BooleanField(default=False)
    github_link = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='project')
    education = models.ForeignKey(
        Education, 
        on_delete=models.SET_NULL,  # If education is deleted, project remains
        null=True, 
        blank=True,  # Allows projects to exist without education
        related_name="projects"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Project"
        ordering = ['-end_date', '-start_date']


class Certificates(models.Model):
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='certificates')

    def __str__(self):
        return f'{self.name} from {self.issuing_organization}'
    
    class Meta:
        ordering = ['-issue_date']
    