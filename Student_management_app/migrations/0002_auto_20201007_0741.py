# Generated by Django 3.0.8 on 2020-10-07 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LeaveFeedbackStudents',
            new_name='FeedbackStudents',
        ),
    ]
