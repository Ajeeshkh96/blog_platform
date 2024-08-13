from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    dob = models.DateField()

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set'
    )
