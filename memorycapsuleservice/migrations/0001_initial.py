# Generated by Django 2.0.13 on 2020-01-16 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capsule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('capsule_id', models.CharField(default='', max_length=128)),
                ('capsule_type', models.CharField(default='', max_length=128)),
                ('capsule_content', models.TextField(default='')),
                ('capsule_time', models.CharField(default='', max_length=128)),
                ('capsule_date', models.CharField(default='', max_length=128)),
                ('capsule_location', models.CharField(default='', max_length=128)),
                ('capsule_person', models.CharField(default='', max_length=128)),
                ('capsule_image', models.CharField(default='', max_length=128)),
                ('capsule_create_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True)),
                ('userpassword', models.CharField(default='', max_length=256)),
                ('useremail', models.EmailField(default='', max_length=254)),
                ('usersex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=32)),
                ('usernickname', models.CharField(default='', max_length=128)),
                ('usertitle', models.CharField(default='', max_length=256)),
                ('usercreatetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
