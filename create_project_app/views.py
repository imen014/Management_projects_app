from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from create_project_app.forms import CreateProjectForm
from django.contrib.auth.decorators import login_required, permission_required
from create_project_app.models import ProjectCreationModel




@permission_required('create_project_app.create_project')
def create_project(request):
    form = CreateProjectForm()
    message = ""
    if request.method=="POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            message = "project created"
    return render(request, 'create_project_app/project.html', {'message':message,'form':form})


@login_required
def get_my_projects(request):
    projects = get_list_or_404(ProjectCreationModel, project_manager=request.user)
    return render(request, 'create_project_app/get_my_projects.html', {'projects':projects})

@permission_required('create_project_app.get_projects')
def get_projects(request):
    projects=ProjectCreationModel.objects.all()
    return render(request, 'create_project_app/get_projects.html', {'projects':projects})


@permission_required('create_project_app.modify_project')
def modify_project(request, id):
    project = get_object_or_404(ProjectCreationModel, id=id)
    form_project = CreateProjectForm(instance=project)
    message = ""
    if request.method == "POST":
        form_project = CreateProjectForm(request.POST, instance=project)
        if form_project.is_valid():
            form_project.save()
            message = "project modified"
    return render(request, 'create_project_app/project_modified.html', {'form_project':form_project,'message':message})

@permission_required('create_project_app.delete_project')
def delete_project(request, id):
    project = get_object_or_404(ProjectCreationModel, id=id)
    project.delete()
    return redirect('get_projects')