from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Patientinfo(models.Model):
    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=False)
    date_of_birth = models.DateField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    street_address = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    provice = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    patient_picture = models.FileField(upload_to="patient_picture/", blank=True, )
    patient_data = models.FileField(upload_to="patient_data/", blank=True, )
    doctor = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname
