from django.contrib import admin
from django.urls import path, re_path, include
from allauth import urls as allauth_urls
from .views import all_other_views
from .views.api_auth_view import ApiLoginAuth, RedirectToAllAuthLogin

app_urlpatterns = [
    path('admin/signup/', all_other_views.index),
    path('admin/', include(allauth_urls)),
    path('admin/api-auth/', ApiLoginAuth.as_view()),
    path('admin/admin-page/login/', RedirectToAllAuthLogin.as_view()),
    path('admin/admin-page/', admin.site.urls),
    re_path(r'^.*$', all_other_views.index)
]
