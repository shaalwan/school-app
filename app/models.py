from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
  registeration_id = models.CharField(primary_key=True,max_length=100)
  name = models.CharField(max_length=500,blank=False)
  father_name = models.CharField(max_length = 500,default='')
  standard = models.IntegerField(validators=[MaxValueValidator(8),MinValueValidator(1)],default=1)
  roll_number = models.IntegerField(default=0)
  is_staff = models.BooleanField(default=False)
