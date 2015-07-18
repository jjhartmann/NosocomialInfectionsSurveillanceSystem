from django.db import models

# Create your models here.

# Table for influenza_na
class Influenza_NA(models.Model):
    genbank_accession_number = models.CharField(max_length=10, null=False, primary_key=True)
    host = models.CharField(max_length=10, null=True)
    genomesegment_or_proteinname = models.CharField(max_length=10, null=True)
    subtype = models.CharField(max_length=10)
    country = models.CharField(max_length=20)  # change to list....
    date_discovered = models.DateField(null=True)
    sequence_length = models.IntegerField(max_length=15)
    virus_name = models.CharField(max_length=30)
    age = models.ImageField(max_length=3)
    gender = models.CharField(max_length=2)    # change to list....

# Table for the Influenza AA
class Influenza_AA(models.Model):
    genbank_accession_number = models.CharField(max_length=10, null=False, primary_key=True)
    host = models.CharField(max_length=10, null=True)
    genomesegment_or_proteinname = models.CharField(max_length=10, null=True)
    subtype = models.CharField(max_length=10)
    country = models.CharField(max_length=20)  # change to list....
    date_discovered = models.DateField(null=True)
    sequence_length = models.IntegerField(max_length=15)
    virus_name = models.CharField(max_length=30)
    age = models.ImageField(max_length=3)
    gender = models.CharField(max_length=2)    # change to list....


class Influenza_FNA(models.Model):
    genbank_na_accnum = models.OneToOneField(Influenza_NA, primary_key=True)
    description = models.CharField(max_length=30)

class Influenza_FAA(models.Model):
    genbank_na_accnum = models.OneToOneField(Influenza_AA, primary_key=True)
    description = models.CharField(max_length=30)





