from django.db import models


class Professor(models.Model):
    first_name = models.CharField(blank=False, max_length=50)
    second_name = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=False, max_length=254)

class Subject(models.Model):
    subject = models.CharField(null = False, blank=False, max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)