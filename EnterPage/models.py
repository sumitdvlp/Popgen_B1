# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Job(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    job_priority=models.IntegerField
    job_name=models.CharField(max_length=50)

    def __str__(self):
        return self.job_name
