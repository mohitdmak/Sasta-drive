from django.db import models
from allauth.socialaccount.models import SocialAccount

#Creating a through model for relating file objects with social account user objects
class Through(models.Model):
    ForUser = models.OneToOneField(SocialAccount, on_delete=models.CASCADE, related_name='filemodels')
    
class FileObject(models.Model):
    Name = models.CharField(max_length=300)
    File = models.FileField(upload_to='documents')
    UserThrough = models.ForeignKey(Through, on_delete=models.CASCADE, related_name='files')


    


