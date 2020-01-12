from django.contrib import admin
from memorycapsuleservice.model.models import Capsule
from memorycapsuleservice.model.models import User

# Register your models here.
admin.site.register(Capsule)
admin.site.register(User)
