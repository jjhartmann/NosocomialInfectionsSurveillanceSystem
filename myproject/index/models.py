from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.

### recreated the UserProfile models in userprofile app ( by Palmer)
# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     profile_picture = models.ImageField(upload_to='profile_image', blank=True)

#     def __unicode__(self):
#         return self.user.username

# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

