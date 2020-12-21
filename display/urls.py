from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.images, name='images'),
    url(r'^home/$', views.home, name='home'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^image/(\d+)', views.image, name='image'),
    url(r'^Silicon_Valley/', views.Silicon_Valley, name='Silicon_Valley')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
