from django.db import models

class Member(models.Model):
	supplierName = models.CharField(max_length=255)
	productName = models.CharField(max_length=255)
	quantity = models.IntegerField(null=True)
	registerDate = models.DateField(null=True)

class SupplierNotification(models.Model):

    productName = models.CharField(max_length=255)
    notificationContent = models.CharField(max_length=255)
    quantity = models.IntegerField(null=True)
    barcode = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.barcode} {self.productName} {self.quantity} "

class PackageLog(models.Model):
    barcode = models.IntegerField(null=True)

    outboundDate = models.DateField(null=True)
    outboundTime = models.TimeField(null=True)

    receivedDate = models.DateField(null=True)
    receivedTime = models.TimeField(null=True)


    def __str__(self):
        return f"{self.barcode} {self.outboundTime} {self.receivedTime}"

class Inventory(models.Model):
    productName = models.CharField(max_length=255)
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.productName} {self.quantity}"

class AllBarcode(models.Model):
    barcode = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.barcode}"
