from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_link = models.URLField(max_length=200)
    project_repo = models.URLField(max_length=200)
    project_image = models.ImageField(upload_to='images/')
    project_descp = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        permissions = [
            ("create_project", "Can add project"),
            ("remove_project", "Can delete project"),
        ]

    def __str__(self):
        return self.project_name


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_date = models.DateField(null=True)
    blog_image = models.ImageField(null=True)
    blog_content = models.TextField()

    def __str__(self):
        return self.blog_title
