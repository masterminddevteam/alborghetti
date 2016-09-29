from rest_framework.routers import DefaultRouter

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^spider/(?P<pk>\d+)/detail$', views.SpiderDetailView.as_view(), name='detail'),
    url(r'^spider/(?P<category>\w+)', views.SpiderCategoryView.as_view(), name='spider-categories'),
]
