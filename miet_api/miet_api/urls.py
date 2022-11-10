from django.contrib import admin
from django.urls import path, include

from iot.views import IotViewSet
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path as url


router=routers.DefaultRouter()
router.register(r'iot', IotViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]


schema_view = get_schema_view(
   openapi.Info(
      title="API для получения информации с датчиков на скважинах",
      default_version='v1',
      description="Документация для API встраиваемых систем Iot проекта miet_api. Лабораторная работа 3 МИЭТ. Реализовал Московский В.В.",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="vld.85@inbox.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', 
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
       name='schema-redoc'),
] 