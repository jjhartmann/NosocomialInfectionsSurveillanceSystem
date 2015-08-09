from django.db import models
from django.forms import ModelForm
# Create your models here.
class contacts(models.Model):
	name = models.CharField (max_length = 200)
	email = models.EmailField (max_length = 254, blank = True)
	phone = models.CharField(max_length = 200, blank = True)
	message = models.CharField (max_length = 500, blank = True)

	def __unicode__(self):
		return u'%s %s' % (self.name, self.email)