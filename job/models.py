from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

JOB_NATURE_CHOICES =(
    ("FullTime","FullTime"),
    ("PartTime","PartTime"),
    )


class Jobs(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='jobs_images')
    location = models.CharField(max_length=150)
    salary = models.IntegerField()
    job_nature =models.CharField(max_length=50 , choices=JOB_NATURE_CHOICES)
    job_descreiption = models.TextField( max_length= 4000)
    posted_date =models.DateTimeField(default=timezone.now )
    vacancy  =models.IntegerField() 
    application_date = models.DateTimeField(default=timezone.now)

class JobRequiredSkills(models.Model):
    skills = models.CharField(max_length=200)
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE,related_name='JobRequiredSkills')
class JobEducation_Experience(models.Model):
    skills = models.CharField(max_length=200)
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE,related_name='JobEducation_Experience')