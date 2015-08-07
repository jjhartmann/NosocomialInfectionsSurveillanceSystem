from django.db import models


# Create your models here.

class FASTATable(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.TextField(null=True)
    fasta = models.TextField(null=True)
