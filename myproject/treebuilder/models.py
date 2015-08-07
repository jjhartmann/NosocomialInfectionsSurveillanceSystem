from django.db import models


# Create your models here.
class TreebuilderFiles(models.Model):
    user = models.CharField(max_length=100, primary_key=True, null=False)
    newick_file = models.TextField(null=True)
    phyloxml_file = models.TextField(null=True)
