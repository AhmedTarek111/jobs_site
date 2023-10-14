# Generated by Django 4.2.6 on 2023-10-14 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobEducation_Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JobRequiredSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='jobs_images')),
                ('location', models.CharField(max_length=150)),
                ('salary', models.IntegerField()),
                ('job_nature', models.CharField(choices=[('FullTime', 'FullTime'), ('PartTime', 'PartTime')], max_length=50)),
                ('job_descreiption', models.TextField(max_length=4000)),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('vacancy', models.IntegerField()),
                ('application_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('education', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.jobeducation_experience')),
                ('skills', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.jobrequiredskills')),
            ],
        ),
    ]