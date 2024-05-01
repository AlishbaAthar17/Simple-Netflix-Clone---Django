from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserNetflix(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    
