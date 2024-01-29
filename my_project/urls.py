"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_project.views import create_user, login_user, home, logout_user, get_users, delete_user, get_user_permissions, create_permission, attribuer_permission, get_permission_per_user, delete_permission, create_group, get_groups, modify_group, delete_group, attribuer_group, attribuerGroupPermission, attribuer_group_user_selon_role, get_users_from_group
from create_project_app.views import create_project, get_my_projects, get_projects, modify_project, delete_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', create_user, name="create_user"),
    path('login_user/', login_user, name="login_user"),
    path('home/', home, name="home"),
    path('logout_user/', logout_user, name="logout_user"),
    path('get_users/', get_users, name="get-users"),
    path('delete_user/<int:id>/delete', delete_user, name="delete-user"),
    path('create_project/', create_project, name="create_project"),
    path('get_user_permissions',get_user_permissions, name="get_user_permissions"),
    path('create_permission/', create_permission, name="create_permission"),
    path('attribuer_permission/', attribuer_permission, name="attribuer_permission"),
    path('get_permission_per_user/<int:id>/', get_permission_per_user, name="get_permission_per_user"),
    path('delete_permission/<int:id>/delete', delete_permission, name="delete_permission"),
    path('get_my_projects/', get_my_projects, name="get_my_projects"),
    path('get_projects/', get_projects, name="get_projects"),
    path('modify_project/<int:id>/', modify_project, name="modify_project"),
    path('delete_project/<int:id>/', delete_project, name="delete_project"),
    path('create_group/', create_group, name="create_group"),
    path('get_groups/', get_groups, name="get_groups"),
    path('modify_group/<int:id>/', modify_group, name="modify_group"),
    path('delete_group/<int:id>/', delete_group, name="delete_group"),
    path('attribuer_group/', attribuer_group, name="attribuer_group"),
    path('attribuerGroupPermission/', attribuerGroupPermission, name="attribuerGroupPermission"),
    path('attribuer_group_user_selon_role/', attribuer_group_user_selon_role, name="attribuer_group_user_selon_role"),
    path('get_users_from_group/<int:id>/', get_users_from_group, name="get_users_from_group"),
]
