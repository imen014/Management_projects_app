from django.shortcuts import render, redirect, get_object_or_404
from app_project.forms import UserCreatorForm, Login_user_form, PermissionCreatorForm, AttribuerPermissionForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from app_project.models import CreatorProjectModel, PermissionCreator
from django.contrib.auth.models import Permission, ContentType
from app_project.models import CreatorProjectModel
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required


def create_user(request):
    form = UserCreatorForm()
    message = ""
    if request.method=="POST":
        form = UserCreatorForm(request.POST)
        if form.is_valid():
            form.save()
            message = "user created !"
            return redirect('home')
    return render(request, 'app_project/user_created.html', {'message':message,'form':form})


def login_user(request):
    form = Login_user_form()
    message = ""
    if request.method == "POST":
        form = Login_user_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                message = "user login success"
                return redirect('home')
            else:
                message = "user is none"
    return render(request, 'app_project/connect.html', {'message':message,'form':form})


@login_required
def home(request):
    return render(request, 'app_project/home.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

@permission_required('app_project.get_users')
def get_users(request):
    users = CreatorProjectModel.objects.all()
    return render(request, 'app_project/users.html', {'users':users})

def delete_user(request, id):
    user = get_object_or_404(CreatorProjectModel, id=id)
    user.delete()
    return redirect('get-users')


def get_user_permissions(request):
    permissions = PermissionCreator.objects.all()
    return render(request, 'app_project/get_permissions.html', {'permissions':permissions})

def create_permission(request):
    form = PermissionCreatorForm()
    message = ""
    if request.method=="POST":
        form = PermissionCreatorForm(request.POST)
        if form.is_valid():
            form.save()
            message = "permission created"
    
    #return redirect('get_user_permissions')
    return render(request, 'app_project/create_permission.html', {'message':message,'form':form})

def attribuer_permission(request):
    form = AttribuerPermissionForm()
    message = ""
    if request.method == "POST":
        form = AttribuerPermissionForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['users']
            permission = form.cleaned_data['permission']
            user.user_permissions.add(permission)
            message = "permission attribué !"
    return render(request, 'app_project/permission_attribuer.html', {'message':message,'form':form})

def get_permission_per_user(request, id):
    user = get_object_or_404(get_user_model(), id=id)
    permissions = user.user_permissions.all()
    return render(request, 'app_project/permissions_per_user.html', {'permissions':permissions,'user':user})

@permission_required('app_project.delete_permission')
def delete_permission(request, id):
    permission = get_object_or_404(PermissionCreator, id=id)
    permission.delete()
    return redirect('get_user_permissions')