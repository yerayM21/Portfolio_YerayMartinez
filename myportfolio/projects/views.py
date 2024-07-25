from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    return render(request,'projects.html',{'projects':projects})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request,'add_project.html',{'form':form})