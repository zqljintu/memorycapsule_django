# Generated by Django 2.2.3 on 2019-09-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorycapsuleservice', '0002_capsule_capsule_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capsule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
