from django import forms
from create_project_app.models import ProjectCreationModel


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectCreationModel
        fields = ['project_name','project_content','project_manager']