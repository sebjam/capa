from django.conf.urls import url, include

from gallery.views import GalleryViewSet, PhotoViewSet
from user_profile.views import UserViewSet

from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

galleries_router = routers.NestedSimpleRouter(
    router,
    r'users',
    lookup='users'
)
galleries_router.register(r'galleries', GalleryViewSet)

photos_router = routers.NestedSimpleRouter(
    galleries_router,
    r'galleries',
    lookup='galleries'
)
photos_router.register(r'photos', PhotoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(galleries_router.urls)),
    url(r'^', include(photos_router.urls)),
]
