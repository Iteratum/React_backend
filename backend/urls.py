from django.urls import path, include
from backend import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('BlogHost', views.BlogHost),
]
