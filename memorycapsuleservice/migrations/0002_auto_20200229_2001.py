# Generated by Django 2.0.13 on 2020-02-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorycapsuleservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capsule',
            name='capsule_image',
            field=models.ImageField(upload_to='capsuleimage/'),
        ),
    ]
