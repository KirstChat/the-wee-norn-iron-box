# Generated by Django 3.2 on 2021-06-17 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='added_by',
            new_name='posted_by',
        ),
    ]
