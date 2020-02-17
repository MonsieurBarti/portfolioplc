from django.urls import path

from portfolio import settings
from .views import HomeTemplateView
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="index"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
]
