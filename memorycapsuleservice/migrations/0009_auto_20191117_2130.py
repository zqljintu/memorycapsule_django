# Generated by Django 2.2.3 on 2019-11-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorycapsuleservice', '0008_auto_20191117_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=32),
        ),
    ]
