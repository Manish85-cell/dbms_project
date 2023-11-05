from django.shortcuts import render
from requests import request
from .serializer import BusSerializer, BusCodesSerializer, RouteSerializer
from rest_framework.generics import ListAPIView
from .models import BusStand, Bus, Routes
# from .models import BusStand
# Create your views here.
class BusStandsList(ListAPIView):
    serializer_class = BusSerializer
    def get_queryset(self):
        code = self.request.GET.get('code')
        if code is not None:
            return BusStand.objects.filter(code = code)
        else:
            return BusStand.objects.all()
       
    
class RouteList(ListAPIView):
    queryset = Routes.objects.all()
    serializer_class = RouteSerializer
   
        
   
class Bus_Codes_List(ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusCodesSerializer


# class Bus_Routes(ListAPIView):
#     inp_code = request.GET.get('inp_code')
    
#     queryset = Bus.objects.raw("SELECT Name FROM route_BusStand WHERE code = (SELECT route FROM route_Bus WHERE bus_code = %s Cross Apply String_split(TAGS, (,))", [inp_code])

#     serializer =_class = RouteSerializer

