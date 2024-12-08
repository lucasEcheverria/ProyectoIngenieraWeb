from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

# Rutas traducibles
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('spotyWebApp/', include('spotyWebApp.urls')),
)

# Incluye set_language
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]

