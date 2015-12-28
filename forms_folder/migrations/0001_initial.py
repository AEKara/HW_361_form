# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=30)),
                ('course_code', models.CharField(max_length=30)),
                ('classroom', models.CharField(max_length=30)),
                ('times', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name_s', models.CharField(max_length=30)),
                ('last_name_s', models.CharField(max_length=30)),
                ('email_add_s', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('office_details', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=12)),
                ('email_add', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='c_students',
            field=models.ManyToManyField(to='forms_folder.Students'),
        ),
        migrations.AddField(
            model_name='courses',
            name='c_teacher',
            field=models.ForeignKey(to='forms_folder.Teachers'),
        ),
    ]
