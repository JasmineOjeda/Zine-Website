from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'article'
urlpatterns = [
	path('', views.article_list, name='article_list'),
	path('<int:article_id>/', views.article, name='article'),
	path('<int:streamhighlight_id>/', views.streamhighlight, name='streamhighlight'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)