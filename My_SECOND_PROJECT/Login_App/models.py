from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    ##user entry will be here
    ## with one to one join
    user        = models.OneToOneField(User,on_delete=models.CASCADE)
    facebook    = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True)


    def __str__(self):
        return self.user.username

