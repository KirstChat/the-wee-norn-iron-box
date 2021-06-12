# Generated by Django 3.2 on 2021-06-12 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_delete_boxsizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
