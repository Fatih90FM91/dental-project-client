
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path('', include('website.urls')),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns (
   
    path('', include('website.urls')),
) + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
