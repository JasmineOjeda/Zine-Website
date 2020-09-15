from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone

from .models import Magazine, Highlight

# Create your views here.

def library(request):
	counter = 0
	latest_magazine_list = Magazine.objects.order_by('-pub_date')
	context = {
		'latest_magazine_list': latest_magazine_list,
	}
	return render(request, 'magazine/library.html', context)


def flipbook(request, magazine_id):
	magazine = get_object_or_404(Magazine, pk=magazine_id)
	
	return render(request, 'magazine/flipbook.html', {'magazine': magazine})

