# Generated by Django 3.2 on 2021-05-16 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_auto_20210516_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu',
            name='desc',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cpu',
            name='dprice',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]