# Generated by Django 3.2 on 2021-05-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_build_pc'),
    ]

    operations = [
        migrations.AddField(
            model_name='build_pc',
            name='image',
            field=models.ImageField(blank='True', default='', null=True, upload_to='uploads/product/'),
        ),
    ]