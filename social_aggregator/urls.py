# social_aggregator/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feeds/', include('feeds.urls')),  # Correctly includes the feeds app URLs
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
