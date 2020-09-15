from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'creator'
urlpatterns = [
	path('', views.creator_list, name='creator_list'),
	path('<int:creator_id>/', views.profile, name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)