from django.contrib import admin
from .models import SupplierNotification , PackageLog, Inventory, AllBarcode
# Register your models here.

admin.site.register(SupplierNotification)
admin.site.register(PackageLog)
admin.site.register(Inventory)
admin.site.register(AllBarcode)