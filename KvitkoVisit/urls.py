from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler403, handler400
from main import views
from django.views.static import serve
# import os
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]

handler404 = views.Error.as_view()
handler500 = views.Error.as_view()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG == False:
#     STATIC_URL = '/static/'
#     MEDIA_URL= '/media/'
#     STATIC_ROOT=os.path.join(BASE_DIR,'/static')
#     MEDIA_ROOT=os.path.join(BASE_DIR,'/media')