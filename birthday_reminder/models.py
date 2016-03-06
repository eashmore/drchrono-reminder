from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Patient(models.Model):
    doctor = models.ForeignKey(User)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    birthday = models.DateTimeField()
    email_bool = models.BooleanField('send_email', default=False)

    def __str__(self):
        return self.email
