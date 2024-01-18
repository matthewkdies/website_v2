from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from website_v2.main.views import (
    BlogDetailView,
    BlogListView,
    ContactFormView,
    ProjectDetailView,
    ProjectListView,
    blog_category,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path( "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("website_v2.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("blog/<slug:slug>/", BlogDetailView.as_view(), name="blog-detail"),
    path("blog/category/<slug:category>/", blog_category, name='categories'),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("projects/<slug:slug>", ProjectDetailView.as_view(), name="project-details"),
    # path("contact/", ContactFormView.as_view(), name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
