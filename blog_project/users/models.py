from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WorkingUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name = "working_user")
    mobile = models.CharField(max_length=15, null=False)
    gender = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    image = models.ImageField(default = 'default.PNG',upload_to='media')
    def __str__(self):
        return self.user.username
