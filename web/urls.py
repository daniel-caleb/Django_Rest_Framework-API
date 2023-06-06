from django.urls import path, include
from app.views import JobViewSet
from app.views import ScrapingView
from rest_framework import routers

rt = routers.DefaultRouter()
rt.register(r'Jobs', JobViewSet)

urlpatterns = [
    path('api/scrape/', ScrapingView.as_view(), name='scraping view'),
    path('', include(rt.urls)),
]
