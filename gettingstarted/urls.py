from django.urls import path, include
from django.contrib import admin
from django.conf import settings  # メディア
from django.conf.urls.static import static  # メディア

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", include("blog.urls")),
    path("", include("account.urls")),
    path("", include("features.urls")),
    path("", include("contact.urls")),
    path('album/', include('album.urls')),
    path("admin/", admin.site.urls),
]

# 開発環境次のみDjangoアプリケーション側でメディアファイルを配信
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
