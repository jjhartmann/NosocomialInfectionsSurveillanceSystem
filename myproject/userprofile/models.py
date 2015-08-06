from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
       )

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to='static/profile_image', blank=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True )
    def __unicode__(self):
        return self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

