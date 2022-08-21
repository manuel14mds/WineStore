from django.contrib import admin
from django.urls import path, include
from wine_project.views import home
from django.conf.urls.static import static
from django.conf import settings
from .views import about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='Home Page'),
    path('wines/', include('wines.urls')),
    path('varietal/', include('varietal.urls')),
    path('winery/', include('winery.urls')),
    path('accounts/', include('users.urls')),
    path('about/', about_us, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
