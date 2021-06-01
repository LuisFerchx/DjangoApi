from ApiApplication.models import Item
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


class ItemApiView(APIView):
    serializers_class=ItemSerializer
    def get(self,request):
        allItems=Item.objects.all().values()
        return Response({"Message":"Lista de Items","Item List": allItems})
    
    def post(self,request):
        print('requiere este dato: ',request.data)
        serializers_obj=ItemSerializer(data=request.data)
        if(serializers_obj.is_valid()):
            Item.objects.create(ite_nombre=serializers_obj.data.get("ite_nombre"),
                                ite_precio=serializers_obj.data.get("ite_precio"),
                                ite_stock=serializers_obj.data.get("ite_stock"))

        item=Item.objects.all().values()
        return Response({"Message":"Agregado correctamente","Item": item})
    