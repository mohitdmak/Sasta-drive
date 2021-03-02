from django.db import models
from django.contrib.auth.models import User

#Creating a through model for relating FileObject model with User object.
class Through(models.Model):
    ForUser = models.OneToOneField(User, on_delete=models.CASCADE, related_name='filemodels')
    
# Creating the FileObject model, which would contain the file name, and the File will be uploaded to 'media/documents/'
# Also, the UserThrough ForeignKey property links the FileObject to the User who uploaded the file.
class FileObject(models.Model):
    Name = models.CharField(max_length=300)
    File = models.FileField(upload_to='documents')
    UserThrough = models.ForeignKey(Through, on_delete=models.CASCADE, related_name='files')


    


