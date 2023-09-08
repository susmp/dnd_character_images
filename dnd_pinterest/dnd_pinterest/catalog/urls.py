from django.urls import path
from . import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image/(?P<pk>\d+)$', views.ImageDetailView.as_view(), name='image-detail'),
    path('upload_image/', views.uploadView, name= 'upload_image'),
    path(r'<slug:tag_slug>/$', views.TagIndexView.as_view(), name = 'images_by_tag'),
]
