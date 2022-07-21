from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, re_path
from django.views.generic import RedirectView
from rest_framework import permissions

urlpatterns = [
    re_path(r"^admin/", admin.site.urls, name="admin"),
    re_path(r"^$", RedirectView.as_view(url="/admin")),
    re_path(
        r"^robots.txt",
        lambda x: HttpResponse(
            "User-Agent: *\n" "Disallow: /", content_type="text/plain"
        ),
        name="robots_file",
    ),
    re_path(r"^silk/", include("silk.urls", namespace="silk")),
]

if settings.ENVIRONMENT == "local":
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view

    schema_view = get_schema_view(
        openapi.Info(
            title="Snippets API",
            default_version="v1",
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )
    urlpatterns += [
        re_path(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"^redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
