# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
GENDER_CHOICES= (
	('Male','Male'),
	('Female','Female'),
	('Other/No Answer','Other/No Answer'),
)

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=16, choices = GENDER_CHOICES, default = 'Other/No Answer')
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.first_name + " " + self.last_name
