from django.db import models
import os
from pdf2image import convert_from_path
from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User

ROLE_CHOICES = (('Editor-in-Chief', 'Editor-in-Chief'),
				('Writer', 'Writer'),
				('Editor','Editor'),
				('Reporter', 'Reporter'),
				('Artist', 'Artist'),
				('Developer', 'Developer')
			)

# Create your models here.
class Role(models.Model):
	title = models.CharField(max_length=100,choices=ROLE_CHOICES, db_index=True)

	def __str__(self):
		return self.title

#TODO: Figure out how to link social media and its type to an image
class SocialMedia(models.Model):
	link = models.CharField(max_length=500, db_index=True)

class Staff(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	profile_pic = models.ImageField(upload_to='staff/profile_pic/', default='staff/profile_pic/default.jpg')
	related_user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=1000, null=True)
	related_role = models.ManyToManyField(Role)
	
	def __str__(self):
		return self.name
	def __unicode__(self):
		return '%s' % self.name
	def get_absolute_url(self):
		return ('view_staff_post', None, { 'slug': self.slug })

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		staff = Staff.objects.create(related_user=instance)
		staff.name = instance.username
		staff.slug = instance.username
		staff.save()

signals.post_save.connect(create_user_profile, sender=User)
