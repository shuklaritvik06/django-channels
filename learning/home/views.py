from django.shortcuts import render
from rest_framework.decorators import api_view
from .thread import CreateData
from django.http import JsonResponse


@api_view(["GET"])
def send_data(request):
    CreateData(10).start()
    return JsonResponse({"message": "Sending Data"})
