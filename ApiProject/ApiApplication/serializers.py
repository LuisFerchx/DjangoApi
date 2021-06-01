from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    ite_nombre = serializers.CharField(label="ingrese el nombre del producto")
    #ite_precio = serializers.DecimalField(label="ingrese un valor numerico")
    #ite_stock = serializers.DecimalField(label="ingrese un valor numerico")