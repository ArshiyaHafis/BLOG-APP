from django.shortcuts import render, get_object_or_404
from .models import Project, Blog
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import RegForm, LoginForm, ProjectForm, BlogForm
from django.contrib.auth.views import LoginView
# Create your views here.


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    blog_data = Blog.objects.all().order_by('blog_date')
    main = {'posts': blog_data, }
    return render(request, 'blog.html', main)


def get_project(request):
    project_data = Project.objects.all().order_by('project_name')
    main = {'projects': project_data, }
    return render(request, 'project.html', main)


def post_project(request):
    form = ProjectForm()
    print("post project")
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            print("saved")
            prj = form.save()
            prj.user = request.user
            prj.save()
            return render(request, 'add_project.html', {'msg': 'Project added successfully'})
        else:
            print("not valid", form.errors.as_data())
            return render(request, 'add_project.html', {'msg': 'Form invalid : '+form.errors.as_data()})
    context = {'form': form}
    return render(request, 'add_project.html', context)


def delete_project(request, name, id):
    print(name)
    print(id)
    project_set = Project.objects.filter(
        project_name=name, user=request.user, id=id)
    if (project_set.count() == 0):
        print("yes")
        return render(request, 'main.html', {'msg': 'not available for deletion'})
    print(project_set)
    project_set.delete()
    return render(request, 'main.html', {'msg': 'deleted successfully'})


def update_project(request, name, id):
    form = ProjectForm()
    print("update project")
    if request.method == 'POST':
        project_set = Project.objects.filter(
            project_name=name, user=request.user, id=id)
        project_set.delete()
        form = ProjectForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            print("saved")
            prj = form.save()
            prj.user = request.user
            prj.save()
            return render(request, 'main.html', {'msg': 'Updated Succesfully'})
        else:
            print("not valid", form.errors.as_data())
            return render(request, 'main.html', {'msg': form.errors.as_data()})
    context = {'form': form}
    return render(request, 'add_project.html', context)


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return render(request, 'main.html', {'msg': 'Registration Successful'})
        else:
            return render(request, 'main.html', {'error': form.errors.items})
    else:
        form = RegForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        # print(form)
        if form.is_valid():
            auth_login(request, form.get_user())
            return render(request, 'main.html', {'msg': 'Login Successful'})
        else:
            print(form.errors.as_data())
            return render(request, 'main.html', {'msg': form.errors.as_data()})
    else:
        form = LoginForm()
    print("enter")
    context = {'form': form}
    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return render(request, 'main.html')


def add_blog(request):
    form = BlogForm()
    print("post project")
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            form.save()
            print("saved")
            return render(request, 'add_blog.html', {'msg': 'Blog added successfully'})
        else:
            print("not valid", form.errors.as_data())
            return render(request, 'add_blog.html', {'msg': 'Form invalid: ' + str(form.errors.as_data())})
    context = {'form': form}
    return render(request, 'add_blog.html', context)


def blogpost(request, title, id):
    print(title)
    print(id)
    blog_set = Blog.objects.filter(
        blog_title = title, id=id)
    if (blog_set.count() == 0):
        print("yes")
        return render(request, 'blog.html', {'msg': 'no blogpost available  '})
    print(blog_set)
    content = {'info':blog_set,}
    return render(request, 'blogpost.html', content)

def del_blog(request, title, id):
    blog_set = Blog.objects.filter(
        blog_title = title, id=id)
    if (blog_set.count() == 0):
        print("yes")
        return render(request, 'blog.html', {'msg': 'not available for deletion'})
    print(blog_set)
    blog_set.delete()
    return render(request, 'blog.html', {'msg': 'deleted successfully'})


def upd_blog(request, title, id):
    blog_set = get_object_or_404(Blog, blog_title=title, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog_set)
        if form.is_valid():
            form.save()
            return render(request, 'blog.html', {'msg': 'updated successfully'})
    else:
        form = BlogForm(instance=blog_set)
    context = {
        'form': form,
        'blog': blog_set,
    }
    return render(request, 'upd_blog.html', context)