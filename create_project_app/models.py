from django.db import models
from app_project.models import CreatorProjectModel

class ProjectCreationModel(models.Model):
    project_name = models.CharField(max_length=50)
    project_content = models.CharField(max_length=150)
    project_manager = models.ForeignKey(CreatorProjectModel, on_delete=models.CASCADE)
