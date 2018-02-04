from django.db import models
from django.utils import timezone


class SchoolRecord(models.Model):
	emis = models.CharField(max_length=9)
	centre_no = models.CharField(max_length=7)
	name = models.CharField(max_length=256)
	# for future, it's better to link to Result class, e.g. Result(year, wrote, pass)
	wrote_2014 = models.PositiveIntegerField(default=0)
	passed_2014 = models.PositiveIntegerField(default=0)
	wrote_2015 = models.PositiveIntegerField(default=0)
	passed_2015 = models.PositiveIntegerField(default=0)
	wrote_2016 = models.PositiveIntegerField(default=0)
	passed_2016 = models.PositiveIntegerField(default=0)
	
	
	def publish(self):
		self.save()

	def __str__(self):
		return ("Name: {0}, 2014 {1}:{2}, 2015 {3}:{4}, 2016 {5}:{6}.".format(self.name, self.wrote_2014,self.passed_2014,self.wrote_2015,self.passed_2015,self.wrote_2016,self.passed_2016))  