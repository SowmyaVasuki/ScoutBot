from django.db import models

# Create your models here.

class Users(models.Model):
	Uid = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=200)
	email  = models.EmailField(max_length=70,blank=True, null= True, unique= True)
	password = models.CharField(max_length=50)

	def __str__(self):
		return str(self.Uid) + ' - ' + self.name

class BotAction(models.Model):
	movement = models.CharField(max_length=20)

	def __str__(self):
		return self.movement

class Coordinates(models.Model):
	latitute = models.FloatField(null=True)
	longitude = models.FloatField(null=True)

	def __str__(self):
		return str(self.latitute) + ' - ' + str(self.longitute)

