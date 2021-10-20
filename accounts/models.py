from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserGroup(models.Model):
    group_name = models.CharField(max_length=500, null=False)


class Permission(models.Model):
    permission_name = models.CharField(max_length=250, null=False)


class UserGroupPermission(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)


