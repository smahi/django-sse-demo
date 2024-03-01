from django.urls import path
from .views import index_page, sse_events


urlpatterns = [
    path('', index_page),
    path('sse/', sse_events)
]
