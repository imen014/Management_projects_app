from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.auth import get_user_model


class CreatorProjectModel(AbstractUser):

    CREATOR = 'créateur'
    SUBSCRIBER = 'Abonné'

    CHOICES = [
        (CREATOR, 'créateur'),
        (SUBSCRIBER, 'Abonné')
    ]
    tel = models.CharField(max_length=15)
    email = models.EmailField()
    role = models.CharField(max_length=50,choices=CHOICES)

       
class PermissionCreator(Permission):
    pass


class AttribuerPermission(models.Model):
    permission = models.ForeignKey(PermissionCreator, on_delete=models.CASCADE)
    users = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class GroupCreator(Group):
    pass

class AttribuerGroupModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    group = models.ForeignKey(GroupCreator, on_delete=models.CASCADE)

class AttribuerGroupPermission(models.Model):
    group = models.ForeignKey(GroupCreator, on_delete=models.CASCADE)
    permission = models.ForeignKey(PermissionCreator, on_delete=models.CASCADE)