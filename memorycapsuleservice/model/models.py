from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Capsule(models.Model):
    id = models.AutoField(primary_key=True)
    capsule_id = models.CharField(max_length=128, default='')
    capsule_type = models.CharField(max_length=128, default='')
    capsule_content = models.TextField(default='')
    capsule_time = models.CharField(max_length=128, default='')
    capsule_date = models.CharField(max_length=128, default='')
    capsule_location = models.CharField(max_length=128, default='')
    capsule_person = models.CharField(max_length=128, default='')
    capsule_image = models.CharField(max_length=128, default='')
    capsule_create_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.id

    def __unicode__(self):
        return self.capsule_id

    def __unicode__(self):
        return self.capsule_type

    def __unicode__(self):
        return self.capsule_content

    def __unicode__(self):
        return self.capsule_time

    def __unicode__(self):
        return self.capsule_create_time

    def __unicode__(self):
        return self.capsule_date

    def __unicode__(self):
        return self.capsule_person

    def __unicode__(self):
        return self.capsule_location

    def __unicode__(self):
        return self.capsule_image

        class Meta:
            ordering = ['-capsule_create_time']


class User(models.Model):
    M = 'male'
    F = 'female'
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    user_name = models.CharField(max_length=128, unique=True)
    user_password = models.CharField(max_length=256, default='')
    user_email = models.EmailField(unique=False, default='')
    user_sex = models.CharField(max_length=32, choices=gender, default=M)
    user_nickname = models.CharField(max_length=128, default='')
    user_title = models.CharField(max_length=256, default='')
    user_create_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.user_name

    def __unicode__(self):
        return self.user_password

    def __unicode__(self):
        return self.user_emailpy

    def __unicode__(self):
        return self.user_sex

    def __unicode__(self):
        return self.user_create_time

    def __unicode__(self):
        return self.user_title

    def __unicode__(self):
        return self.user_nickname

        class Meta:
            ordering = ["user_create_time"]
            verbose_name = "用户"
            verbose_name_plural = "用户"
