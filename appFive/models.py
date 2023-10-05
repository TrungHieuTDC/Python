from django.db import models

# Create your models here.
class UserInfoApp(models.Model):
    user = models.CharField(max_length=264)
    email = models.CharField(max_length=264,unique=True)
    password = models.CharField(max_length=264)

    def __str__(self):
        return self.user

class UserProfileInfoApp(models.Model):
    user_info = models.OneToOneField(UserInfoApp, on_delete=models.CASCADE)
    #additional
    profile_site_app = models.URLField(blank=True)
    profile_pic_app  = models.ImageField(upload_to='profile_pic_app',blank=True)

    def __str__(self):
        return self.user_info.email
    
