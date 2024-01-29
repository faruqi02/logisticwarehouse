from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),

    path('loginPage/',views.loginPage,name='loginPage'),
    path('registerPage/',views.registerPage,name='registerPage'),
    path('logoutPage/',views.logoutUser,name='logoutPage'),

    path('supplier-dashboard/',views.supplierDashboard,name='supplierDashboard'),
    path('manager-dashboard/',views.managerDashboard,name='managerDashboard'),
    path('staff-dashboard/',views.staffDashboard,name='staffDashboard'),
    path('client-dashboard/',views.clientDashboard,name='clientDashboard'),

    path('barcode-scanner/', views.barcodeScanner, name='barcodeScanner'),
    path('sidebar/', views.sidebar,name='sidebar'),
    path('barcode-generator/',views.barcodeGenerator,name = 'barcodeGenerator'),
    path('register-barcode/',views.registerBarcode,name='registerBarcode'),

    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('manager-dashboard/delete/<int:id>/',views.delete,name="delete"),
    path('manager-dashboard/update/<int:id>/',views.update,name="update"),
    path('manager-dashboard/update/uprec/<int:id>/',views.uprec,name="uprec"),

    path('delete_by_barcode/', views.deleteBarcode, name='delete_by_barcode'),
    path('manager-dashboard/update-inventory/<int:id>/',views.updateInventory,name='update-inventory'),
    path('manager-dashboard/update-inventory/uprec/<int:id>/',views.uprecInventory,name="uprecInventory"),

    path('update_by_barcode/', views.updateBarcodeReceived, name='update_by_barcode'),
    path('outbound_by_barcode/', views.updateBarcodeOutbound, name='outbound_by_barcode'),

    path('RegisterPackage/', views.RegisterPackage, name='RegisterPackage'),

    path("add-inventory",views.addInventory,name="add-inventory"),
    path('staff-dashboard/delete-inventory/<int:id>/',views.deleteInventoryStaff,name="delete-inventory"),
    path('staff-dashboard/update-inventory/<int:id>/',views.updateInventoryStaff,name='update-inventory'),
    path('staff-dashboard/update-inventory/uprec/<int:id>/',views.uprecInventoryStaff,name='uprecInventory'),

]