from django import forms
from models import Patientinfo

class PatientinfoForm(forms.ModelForm):

        class Meta:
                model = Patientinfo
                fields = ('firstname',
                          'lastname',
                          'date_of_birth',
                          'gender',
                          'age',
                          'email',
                          'phone',
                          'street_address',
                          'city',
                          'provice',
                          'postal_code',
                          'patient_picture',
                          'patient_data'                          
                          )

class PatientDataForm(forms.ModelForm):


        class Meta:
                model = Patientinfo
                fields = ('patient_data',)
