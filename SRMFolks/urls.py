from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from SRMFolks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='homePage'),
    path('events/', views.eventsPage, name='eventsPage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
