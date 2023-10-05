from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.email

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #additional
    profile_site = models.URLField(blank=True)
    profile_pic  = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.email
    
