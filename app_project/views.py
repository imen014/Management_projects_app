from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from app_project.forms import UserCreatorForm, Login_user_form, PermissionCreatorForm, AttribuerPermissionForm, GroupCreatorForm, AttribuerGroupForm, AttribuerGroupPermissionForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from app_project.models import CreatorProjectModel, PermissionCreator, GroupCreator
from django.contrib.auth.models import Permission, ContentType
from app_project.models import CreatorProjectModel
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from app_project.models import GroupCreator
from app_project.RolesAttributor import RolesAttributor


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

def create_group(request):
    group_form = GroupCreatorForm()
    message = ""
    if request.method=="POST":
        group_form = GroupCreatorForm(request.POST)
        if group_form.is_valid():
            group_form.save()
            message = "group created"
    return render(request, 'app_project/create_group.html', {'group_form':group_form,'message':message})

def get_groups(request):
    groups = GroupCreator.objects.all()
    return render(request, 'app_project/groups.html', {'groups':groups})

def modify_group(request, id):
    group = get_object_or_404(GroupCreator, id=id)
    modificator_group_form = GroupCreatorForm(instance=group)
    message = ""
    if request.method=="POST":
        modificator_group_form = GroupCreatorForm(request.POST, instance=group)
        if modificator_group_form.is_valid():
            modificator_group_form.save()
            message = "group modified succefully !"
            return redirect('get_groups')
    return render(request, 'app_project/group_modified.html', {'message':message, 'modificator_group_form':modificator_group_form})

def delete_group(request, id):
    group = get_object_or_404(GroupCreator, id=id)
    group.delete()
    return redirect('get_groups')

def attribuer_group(request):
    form = AttribuerGroupForm()
    user = None
    group = None
    if request.method == "POST":
        form = AttribuerGroupForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']
            user = form.cleaned_data['user']
            if user and group:
                group.user_set.add(user)
    return render(request, 'app_project/group_attributed.html', {'user':user,'group':group,'form':form})

def attribuerGroupPermission(request):
    form = AttribuerGroupPermissionForm()
    group = None
    permission = None
    message = ""
    if request.method == "POST":
        form = AttribuerGroupPermissionForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']
            permission = form.cleaned_data['permission']
            group.permissions.add(permission)
            group.save()
            message = "permission attributed to group"
    return render(request, 'app_project/permission_group_attributed.html', {'message':message,'group':group,'permission':permission, 'form':form})

def attribuer_group_user_selon_role(request):
    users = get_list_or_404(get_user_model())
    group1 = GroupCreator.objects.get(name="CREATOR")
    group2 = GroupCreator.objects.get(name="SUBSRIBER")
    message = ""
    for user in users:
        if user.role == "créateur" or user.role=="CREATOR":
            group1.user_set.add(user)
        elif user.role == "Abonné" or user.role=="SUBSCRIBER":
            group2.user_set.add(user)
        else:
            message = "verify user role !"
    return render(request, 'app_project/user_group_attributed.html', {'message':message,'users':users, 'group1':group1,'group2':group2})

def get_users_from_group(request, id):
    group = get_object_or_404(GroupCreator, id=id)
    users_in_group = group.user_set.all()
    return render(request, 'app_project/users_in_group.html', {'group':group,'users_in_group':users_in_group})