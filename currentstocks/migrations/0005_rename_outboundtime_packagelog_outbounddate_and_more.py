# Generated by Django 5.0.1 on 2024-01-27 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currentstocks', '0004_packagelog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packagelog',
            old_name='outboundTime',
            new_name='outboundDate',
        ),
        migrations.RenameField(
            model_name='packagelog',
            old_name='receivedTime',
            new_name='receivedDate',
        ),
    ]
