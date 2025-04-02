# Generated by Django 4.1.13 on 2023-12-10 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0002_delete_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('photo', models.ImageField(upload_to='user_photos/')),
                ('aadhar', models.CharField(max_length=12)),
                ('aadhar_photo', models.ImageField(upload_to='aadhar_photos/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('license_id', models.CharField(max_length=20)),
                ('enrollment_date', models.DateField()),
                ('license_photo', models.ImageField(upload_to='license_photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('photo', models.ImageField(upload_to='user_photos/')),
                ('aadhar', models.CharField(max_length=12)),
                ('aadhar_photo', models.ImageField(upload_to='aadhar_photos/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('photo', models.ImageField(upload_to='user_photos/')),
                ('aadhar', models.CharField(max_length=12)),
                ('aadhar_photo', models.ImageField(upload_to='aadhar_photos/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('license_id', models.CharField(max_length=20)),
                ('enrollment_date', models.DateField()),
                ('license_photo', models.ImageField(upload_to='license_photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
