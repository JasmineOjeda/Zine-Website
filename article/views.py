from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import StreamHighlight, Article

# Create your views here.

def article_list(request):
	latest_magazine_list = Magazine.objects.order_by('pub_date')
	context = {
		'latest_magazine_list': latest_magazine_list
	}
	return render(request, 'magazine/library.html', context)


def article(request, magazine_id):
	article = get_object_or_404(Article, pk=article_id)
	
	return render(request, 'magazine/article.html', {'article': article})

def streamhighlight(request, streamhighlight_id):
	highlight = get_object_or_404(StreamHighlight, pk=streamhighlight_id)
	
	return render(request, 'magazine/article.html', {'article': highlight})
