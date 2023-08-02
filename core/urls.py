from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static

from users import router as users_api_router
from house import router as house_api_router
from task import router as task_api_router

api_auth_urlpatterns = [
    re_path(r'', include('oauth2_provider.urls', namespace='oauth2_provider')),
]


if settings.DEBUG:
    api_auth_urlpatterns.append(
        path(r'verify/', include('rest_framework.urls'))
    ),

api_urlpatterns = [
    path(r'auth/', include(api_auth_urlpatterns)),
    path(r'accounts/', include(users_api_router.router.urls)),
    path(r'house/', include(house_api_router.router.urls)),
    path(r'tasks/', include(task_api_router.router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
