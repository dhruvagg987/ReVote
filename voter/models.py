from django.db import models

# Create your models here.
class Voter(models.Model):
    # id=models.AutoField()
    username = models.CharField(max_length=20)
    number = models.IntegerField()