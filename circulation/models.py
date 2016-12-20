from django.db import models

# Create your models here.
class CheckOuts(models.Model):
	roll = models.CharField(max_length=20)
	accn_no = models.CharField(max_length=20)
	time_stamp = models.DateTimeField()
