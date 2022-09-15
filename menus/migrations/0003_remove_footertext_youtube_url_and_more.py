# Generated by Django 4.0.7 on 2022-09-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_footertext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footertext',
            name='youtube_url',
        ),
        migrations.AddField(
            model_name='footertext',
            name='pinterest_url',
            field=models.URLField(blank=True, null=True, verbose_name='pinterest'),
        ),
    ]