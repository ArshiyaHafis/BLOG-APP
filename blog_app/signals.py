from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def assign_default_permissions(sender, instance, created, **kwargs):
    if created:
        # Assign permission to the user
        permission = Permission.objects.get(codename='create_project')
        instance.user_permissions.add(permission)
        permission = Permission.objects.get(codename='remove_project')
        instance.user_permissions.add(permission)

        # Assign permission to a group
        group = Group.objects.get(name='project_managers')
        instance.groups.add(group)
