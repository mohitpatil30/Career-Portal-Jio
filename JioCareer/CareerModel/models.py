from django.db import models

# Create your models here.

class Family(models.Model):
	name = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Family'
		verbose_name_plural = "Families"

class Role(models.Model):
	name = models.CharField(max_length = 100)
	family = models.ForeignKey(Family,on_delete = models.CASCADE)
	next_roles = models.ManyToManyField("self",blank = True,symmetrical = False)
	qualification = models.TextField()
	skills = models.TextField()
	responsibilities = models.TextField()
	training = models.TextField()
	experience = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Role'
		verbose_name_plural = "Roles"
