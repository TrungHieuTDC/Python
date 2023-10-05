from django.contrib import admin

# Register your models here.
from appFive.models import UserInfoApp,UserProfileInfoApp


class OrderInfoAppModel(admin.ModelAdmin):
    #order field
    fields = ('email','user','password')
    #adding search 
    search_fields = ('email','user')
    #adding field
    list_display = ('user','email','password')
    #Enable List View 
    list_editable = ('email', 'password')

admin.site.register(UserInfoApp,OrderInfoAppModel)
admin.site.register(UserProfileInfoApp)
