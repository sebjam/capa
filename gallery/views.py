from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from rest_framework import permissions, viewsets


from gallery.mixins import (
    DetailAuthZMixin,
    DetailChildAuthZMixin,
    ListAuthZMixin
)
from gallery.models import Gallery, Photo
from gallery.serializers import GallerySerializer, PhotoSerializer


# Regular Views
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


class CreateGalleryView(CreateView):
    model = Gallery
    fields = ['title', 'description', 'user']


class ListGalleryView(ListAuthZMixin, ListView):
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super(ListGalleryView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DetailGalleryView(DetailAuthZMixin, DetailView):
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super(DetailGalleryView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreatePhotoView(CreateView):
    model = Photo
    fields = ['title', 'description', 'image']

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.gallery = get_object_or_404(Gallery, pk=self.kwargs.get('pk'))
        photo.save()
        return super(CreatePhotoView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail_gallery', kwargs={'pk': self.kwargs.get('pk')})


class DetailPhotoView(DetailChildAuthZMixin, DetailView):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super(DetailPhotoView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


# API Views
class PhotoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
