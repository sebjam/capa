from django.conf.urls import url, include

from gallery.views import GalleryViewSet, PhotoViewSet

from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'galleries', GalleryViewSet)
photos_router = routers.NestedSimpleRouter(
    router,
    r'galleries',
    lookup='galleries'
)
photos_router.register(r'photos', PhotoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(photos_router.urls)),
]
