from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'magazine'
urlpatterns = [
	path('', views.library, name='library'),
	path('<int:magazine_id>/', views.flipbook, name='flipbook'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)