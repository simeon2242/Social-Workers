from django.urls import path

from .api_urls import router


urlpatterns = []
urlpatterns += router.urls