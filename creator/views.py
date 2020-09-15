from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Creator
from article.models import StreamHighlight

# Create your views here.

def creator_list(request):
	creator_list = Creator.objects.order_by('name')
	context = {
		'creator_list': creator_list
	}
	return render(request, 'creator/list.html', context)

def profile(request, creator_id):
	creator = get_object_or_404(Creator, pk=creator_id)
	related_highlights = StreamHighlight.objects.filter(related_creator=creator)
	
	return render(request, 'creator/profile.html', {'creator': creator
													'related_highlights' = related_highlights})
