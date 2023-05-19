from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import my_views

urlpatterns = [
    path('', my_views.index, name='index'),
    path('', include('back.urls')),
    path('admin/', admin.site.urls),
    path('turnos/', include('turnos.urls')),
    path('crear/', my_views.crear_turno, name='crear_turno'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
