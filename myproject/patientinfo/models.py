from django.db import models

# Create your models here.
GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),)

class Patientinfo(models.Model):
	firstname = models.CharField(max_length=20, null=False)
	lastname = models.CharField(max_length=20, null=False)
	date_of_birth= models.DateField(max_length=20, null=True)
        gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True )
        age = models.PositiveSmallIntegerField( null=True)
	email = models.EmailField(max_length=50, null=True)
	phone = models.CharField(max_length=20, null=True)
	street_address = models.CharField(max_length=20, null=True)
	city = models.CharField(max_length=20, null=True)
	provice = models.CharField(max_length=20, null=True)
	postal_code = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.firstname + " " + self.lastname
