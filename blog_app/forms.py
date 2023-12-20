from django.forms import ModelForm
from .models import Project, Blog
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'project_link', 'project_repo',
                  'project_image', 'project_descp',)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_date', 'blog_image', 'blog_content', )
