# Generated by Django 3.0.2 on 2020-09-01 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_total_leaves_left'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='emp_type',
        ),
    ]
