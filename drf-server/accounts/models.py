from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    status_message = models.TextField(null=True, blank=True)
    profile_image_path = models.CharField(max_length=200)
    watching_movie_id = models.ForeignKey(Movie, on_delete=models.SET_DEFAULT, default='')
    status1 = models.CharField(max_length=50)
    status2 = models.CharField(max_length=50)
    status3 = models.CharField(max_length=50)
    status1_gage = models.IntegerField()
    status2_gage = models.IntegerField()
    status3_gage = models.IntegerField()
    acorn = models.IntegerField()
    # background_theme = models.ForeignKey('Theme', on_delete=models.SET_DEFAULT, default=Theme.objects.get(name="default").pk)

class Theme(models.Model):
    price = models.IntegerField()
    source = models.CharField(max_length=200) # 테마 이미지 경로