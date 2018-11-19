
from django.urls import path

from .views import index_view, DeviceView

urlpatterns = [
    # path('api/', include('api.urls')),
    path("index/", index_view),
    path("device/<device_name>/", DeviceView.as_view())
]
