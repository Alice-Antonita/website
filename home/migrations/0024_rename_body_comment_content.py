# Generated by Django 5.1 on 2024-09-16 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
    ]
