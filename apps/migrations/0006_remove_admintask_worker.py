# Generated by Django 5.1.3 on 2024-11-15 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_admintask_worker_alter_admintask_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admintask',
            name='worker',
        ),
    ]