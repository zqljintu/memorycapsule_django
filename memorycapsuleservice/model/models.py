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
    capsule_image = models.ImageField(upload_to='capsuleimage/')
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
    username = models.CharField(max_length=128, unique=True)
    userpassword = models.CharField(max_length=256, default='')
    useremail = models.EmailField(unique=False, default='')
    usersex = models.CharField(max_length=32, choices=gender, default=M)
    usernickname = models.CharField(max_length=128, default='')
    usertitle = models.CharField(max_length=256, default='')
    userimg = models.ImageField(upload_to='userimage/',default= '')
    usercreatetime = models.DateTimeField(default=timezone.now)
    userlogintime = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return self.username

    def __unicode__(self):
        return self.userpassword

    def __unicode__(self):
        return self.useremail

    def __unicode__(self):
        return self.usersex

    def __unicode__(self):
        return self.usercreatetime

    def __unicode__(self):
        return self.usertitle

    def __unicode__(self):
        return self.usernickname

        class Meta:
            ordering = ["usercreatetime"]
            verbose_name = "用户"
            verbose_name_plural = "用户"
