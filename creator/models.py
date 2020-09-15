from django.db import models

# Create your models here.

class Creator(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	slug = models.CharField(max_length=100, db_index=True)
	profile_pic = models.ImageField(upload_to='creator/profile_pic', null=True)
	twitch_link = models.CharField(max_length=500, db_index=True)

	def __unicode__(self):
		return '%s' % self.name
	def get_absolute_url(self):
		return ('view_creator_profile', None, {'slug', self.slug })
	def __str__(self):
		return self.name
