from django.conf.urls import url, include

from gallery.views import GalleryViewSet, PhotoViewSet

from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'galleries', GalleryViewSet)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
