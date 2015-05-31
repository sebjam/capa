from gallery.views import GalleryViewSet, PhotoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'galleries', GalleryViewSet)
router.register(r'photos', PhotoViewSet)router.register(r'photos', PhotoViewSet)
