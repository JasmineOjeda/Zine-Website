import datetime

from django.db import models
from creator.models import Creator
from staff.models import Staff
from django.utils import timezone

# Create your models here.
CATEGORY_CHOICES = ( ('All', 'All'),
				('News', 'News'),
				('Events', 'Events'),
				('SMPs','SMPs'),
				('Discover', 'Discover')
			)

class Category(models.Model):
	title = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, db_index=True)
	slug = models.SlugField(max_length=100, null=True, db_index=True)

	def __unicode__(self):
		return '%s' % self.title
	def get_absolute_url(self):
		return ('view_article_category', None, { 'slug': self.slug })
	def __str__(self):
		return self.title

class ArticleInfo(models.Model):
	title = models.CharField(max_length=100, null=True, unique=True)
	slug = models.SlugField(max_length=100, null=True, unique=True)
	body = models.TextField(null=True)
	thumbnail = models.ImageField(upload_to='article/thumbnail', null=True)

	contributors = models.ManyToManyField(Staff)
	
	pub_date = models.DateTimeField('date published', null=True)
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	class Meta:
		abstract = True

	def __unicode__(self):
		return '%s' % self.title
	def get_absolute_url(self):
		return ('view_article_post', None, { 'slug': self.slug })
	def __str__(self):
		return self.title

class StreamHighlight(ArticleInfo):
	related_creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

class Article(ArticleInfo):
	related_category = models.ManyToManyField(Category)

class ArticleImage(models.Model):
	related_article = models.ForeignKey(Article, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='article/images', null=True)
	description = models.CharField(max_length=500, null=True, unique=True)

	def __str__(self):
		return self.description

class HighlightImage(models.Model):
	related_article = models.ForeignKey(StreamHighlight, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='article/images', null=True)
	description = models.CharField(max_length=500, null=True, unique=True)

	def __str__(self):
		return self.description