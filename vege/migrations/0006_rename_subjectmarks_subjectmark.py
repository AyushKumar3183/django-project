# Generated by Django 5.1.1 on 2024-10-14 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_rename_sunjectmarks_subjectmarks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubjectMarks',
            new_name='SubjectMark',
        ),
    ]
