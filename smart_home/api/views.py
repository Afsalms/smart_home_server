

from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import Device
from .serializers import DeviceSerializer



def index_view(request):
	device = Device.objects.first()
	if request.method == "POST":
		current_status = request.POST.get("current_status")
		if current_status and current_status== 'True':
			device.status = False
			device.save()
		else:
			device.status = True
			device.save()
	return render(request, "api/test.html", {"device": device})


class DeviceView(generics.GenericAPIView):

	def get(self, request, *args, **kwargs):
		try:
			device = Device.objects.get(name=kwargs.get("device_name"))
			serializer = DeviceSerializer(device)
			return Response({"status": "1", "data": serializer.data})
		except Device.DoesNotExist:
			return Response({"status": "-1"}, status=status.HTTP_404_NOT_FOUND)

