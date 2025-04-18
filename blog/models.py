from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

def upload_path(instance, filename):
    # Creates path like: uploads/posts/filename
    return f'uploads/posts/{filename}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_path, null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title