from django.urls import re_path, include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api.consts import OptionalSlashRouter
from api.v1 import views

schema_view = get_schema_view(
   openapi.Info(
      title="Logs API",
      default_version='v1',
      description="This is the API for Discord Log Viewer.",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = OptionalSlashRouter()
router.register(r'logs', views.LogViewSet, basename='logs')

urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', include(router.urls))
]
