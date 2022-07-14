from django.urls import re_path, include
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import RedirectView


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
