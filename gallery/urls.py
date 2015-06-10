# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import (
    CreateGalleryView,
    CreatePhotoView,
    DetailGalleryView,
    HomePageView,
    ListGalleryView
)

urlpatterns = patterns(
    '',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(
        r'^gallery/create/',
        CreateGalleryView.as_view(),
        name='create_gallery'
    ),
    url(
        r'^gallery/(?P<pk>[-\w]+)/$',
        DetailGalleryView.as_view(),
        name='detail_gallery'
    ),
    url(
        r'^gallery/(?P<pk>[-\w]+)/photo/create',
        CreatePhotoView.as_view(),
        name='create_photo'
    ),
    url(r'^gallery/', ListGalleryView.as_view(), name='list_gallery'),
)
