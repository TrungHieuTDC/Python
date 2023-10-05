from django.contrib import admin

# Register your models here.
from first_app.models import User,UserProfileInfo

admin.site.register(User)
admin.site.register(UserProfileInfo)
