from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_name(name):
    m = re.match('[a-zA-Z]+', name)
    if m.group()!=name:
        raise ValidationError("Name should contains only alphabet")
    return name


class Professor(models.Model):
    first_name = models.CharField(blank=False, max_length=50, validators=[validate_name])
    second_name = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=False, max_length=254)

    def __str__(self):
        return self.first_name

class Subject(models.Model):
    subject = models.CharField(null = False, blank=False, max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject