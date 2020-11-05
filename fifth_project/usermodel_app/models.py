from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profilepic',blank=True)

    def __str__(self):
        return self.user.username
