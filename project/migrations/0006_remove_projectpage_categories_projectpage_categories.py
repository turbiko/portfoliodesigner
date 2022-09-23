# Generated by Django 4.0.7 on 2022-09-23 10:00

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_projectcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='categories',
        ),
        migrations.AddField(
            model_name='projectpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='project.projectcategory'),
        ),
    ]
