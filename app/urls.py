from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import RedirectView


urlpatterns = [
    url(r"^$", RedirectView.as_view(url="/admin")),
    url(r"^admin/", admin.site.urls, name="admin"),
    url(
        r"^robots.txt",
        lambda x: HttpResponse(
            "User-Agent: *\n" "Disallow: /", content_type="text/plain"
        ),
        name="robots_file",
    ),
]
