# Generated by Django 4.2.11 on 2024-04-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CattegoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
                ('cattegory_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='HomeCattegoryWiseShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cattegoryWiseImage', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
                ('Course_name', models.CharField(blank=True, max_length=150, null=True)),
                ('Course_fee', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeCattegoryWiseShowsec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CattegoryName', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
            ],
        ),
        migrations.CreateModel(
            name='HomeExpertTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
                ('Teacher_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Position_name', models.CharField(blank=True, max_length=100, null=True)),
                ('institute_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeInstituteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BannerTitle', models.CharField(blank=True, max_length=150, null=True)),
                ('BannerText', models.TextField(blank=True, null=True)),
                ('Banner_image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
            ],
        ),
        migrations.CreateModel(
            name='HomeOurService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_text', models.TextField(blank=True, null=True)),
                ('service_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ServicePlayImage', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
                ('SercicebannerImage', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
                ('Sercicebannervideo', models.FileField(blank=True, null=True, upload_to='Deshboard/media/video')),
            ],
        ),
        migrations.CreateModel(
            name='HomeSeminerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveIntegerField()),
                ('month', models.CharField(blank=True, max_length=20, null=True)),
                ('year', models.PositiveIntegerField()),
                ('seminer_image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
            ],
        ),
        migrations.CreateModel(
            name='HomeStudentOpenion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_image', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
                ('Student_name', models.CharField(blank=True, max_length=50, null=True)),
                ('openion_course_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Openion_text', models.TextField()),
            ],
        ),
    ]
