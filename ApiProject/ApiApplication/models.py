from django.db import models

# Create your models here.
class Item(models.Model):
    ite_id = models.AutoField(primary_key=True)
    ite_nombre = models.CharField(max_length=-1, blank=True, null=True)
    ite_precio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ite_stock = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ite_estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'