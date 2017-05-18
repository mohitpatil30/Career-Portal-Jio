from django.db import models
from django.contrib.auth.models import User
from CareerModel.models import Role,Family
# Create your models here.
	

class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.ForeignKey(Role,on_delete = models.CASCADE)
	experience = models.IntegerField(default = 0)
	skills = models.TextField()
	qualifications = models.TextField()
	competencies = models.TextField()
	achievements = models.TextField()
	def get_fullname(self):
		return str(user.firstname + ' ' + user.lastname)
	
	def __str__(self):
		return self.user.username