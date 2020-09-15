import datetime

from django.db import models
from django.utils import timezone
import os
from pdf2image import convert_from_path
from django.db.models import signals
from django.dispatch import receiver
from django.conf import settings
from django.templatetags.static import static

# Create your models here.

class Magazine(models.Model):
	headline = models.CharField(max_length=100, null=True, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	cover = models.ImageField(upload_to='magazine/covers', null=True)
	magazine_file = models.FileField(upload_to='magazine/pdf_files', null=True)

	pub_date = models.DateTimeField('date published', null=True)
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	def __str__(self):
		return self.headline
	def __unicode__(self):
		return '%s' % self.headline
	def get_absolute_url(self):
		return ('view_magazine_post', None, { 'slug': self.slug })

class Highlight(models.Model):
	related_magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
	content = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.content

@receiver(signals.post_save, sender=Magazine)
def make_magazine(sender, instance, created, **kwargs):
	page_count = 1
	pages = convert_from_path("media/" + str(instance.magazine_file.name))
	for page in pages:
		page.save('magazine/static/magazine/pages/' + instance.slug + str(page_count) + '.jpg', 'JPEG')
		page_count += 1