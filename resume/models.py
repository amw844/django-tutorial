from django.db import models
from django.conf import settings

# Create your models here.
class Resume(models.Model):
    email = models.EmailField()
    personal_summary = models.TextField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=12)
    display_name = models.CharField(max_length=200)

class Education(models.Model):
    resume = models.ForeignKey(Resume, default=None, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=200)
    school_start_date = models.DateField()
    school_end_date = models.DateField()
    best_subject = models.CharField(max_length=200)

class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, default=None, on_delete=models.CASCADE)
    job_role_or_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    job_description = models.TextField()
    job_start_date = models.DateField()
    job_end_date = models.DateField()

class Hobby(models.Model):
    resume = models.ForeignKey(Resume, default=None, on_delete=models.CASCADE)
    interest_or_hobby = models.TextField()
