from django.http import HttpResponse
from django.template import loader
from .models import SupplierNotification, PackageLog, Inventory, AllBarcode
from django.shortcuts import render, redirect
from datetime import date ,datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

########################################################
def registerPage(request):

    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('loginPage')

        context = {
            'form':form,
        }
        return render(request,'registerPage.html',context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('main')
    else:      
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user);
                return redirect('main')
            else:
                messages.info(request,'Username or Password is incorrect')
                #return render(request,'loginPage.html',context)
        context = {
        }
        return render(request,'loginPage.html',context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

#########################################################
@login_required(login_url='loginPage')
def main(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render())

def sidebar(request):
	template = loader.get_template('sidebar.html')
	return HttpResponse(template.render())

def barcodeScanner(request):
	template = loader.get_template('barcode-scanner.html')
	return HttpResponse(template.render())

def barcodeGenerator(request):
	template = loader.get_template('barcode-generator.html')
	return HttpResponse(template.render())

def registerBarcode(request):
	template = loader.get_template('register-barcode.html')
	return HttpResponse(template.render())

def supplierDashboard(request):
	notification = SupplierNotification.objects.all().values()
	template = loader.get_template('supplier-dashboard.html')
	return HttpResponse(template.render({'notification': notification},request))

def deleteBarcode(request):
    if request.method == 'POST':
        barcode_to_delete = request.POST.get('barcode_to_delete', '')

        # Check if a barcode is provided
        if barcode_to_delete:
            # Delete records with the given barcode
            SupplierNotification.objects.filter(barcode=barcode_to_delete).delete()
            AllBarcode.objects.filter(barcode=barcode_to_delete).delete()

            # Redirect to a success page or any other appropriate page
            return redirect('../supplier-dashboard/')

    #return render(request, 'delete_by_barcode.html')

def updateBarcodeReceived(request):
    if request.method == 'POST':
        barcode_to_update = request.POST.get('barcode_to_update', '')

        # Check if a barcode is provided
        if barcode_to_update:
            # Update records with the given barcode that receivedDate is today
            PackageLog.objects.filter(barcode=barcode_to_update).update(
                receivedDate=date.today(),
                receivedTime=datetime.now().time()
            )

            # Redirect to a success page or any other appropriate page
            return redirect('../client-dashboard/')

def updateBarcodeOutbound(request):
    if request.method == 'POST':
        barcode_to_outbound = request.POST.get('barcode_to_outbound', '')

        # Check if a barcode is provided
        if barcode_to_outbound:
            # Update records with the given barcode that receivedDate is today
            PackageLog.objects.filter(barcode=barcode_to_outbound).update(
                outboundDate=date.today(),
                outboundTime=datetime.now().time()
            )

            # Redirect to a success page or any other appropriate page
            return redirect('../staff-dashboard/')
        return redirect('../staff-dashboard/')
    return redirect('../staff-dashboard/')

def managerDashboard(request):
    notification = SupplierNotification.objects.all().values()
    packagelog = PackageLog.objects.all().values()
    inventory = Inventory.objects.all().values()
    barcode = AllBarcode.objects.all().values()
    form = CreateUserForm(request.POST)
    template = loader.get_template('manager-dashboard.html')

    inventory_data = Inventory.objects.all()
    context = {
    	'notification' : notification,
    	'packagelog' : packagelog,
    	'inventory' : inventory,
        'barcode' : barcode,
        'form' : form,
        'inventory_data' : inventory_data,
    }
    return HttpResponse(template.render(context,request))

def staffDashboard(request):
    notification = SupplierNotification.objects.all().values()
    packagelog = PackageLog.objects.all().values()
    inventory = Inventory.objects.all().values()
    template = loader.get_template('staff-dashboard.html')
    context = {
        'notification': notification,
        'packagelog':packagelog,
        'inventory':inventory
    }
    return HttpResponse(template.render(context,request))

def clientDashboard(request):
    notification = SupplierNotification.objects.all().values()
    packagelog = PackageLog.objects.all().values()
    template = loader.get_template('client-dashboard.html')
    context = {
        'notification' : notification,
        'packagelog' : packagelog
    }
    return HttpResponse(template.render(context,request))

###########################################

def add(request):
    return render(request,'add-notification.html')

def addInventory(request):
    productName = request.POST['productName']
    quantity = request.POST['quantity']
    price = request.POST['price']
    inventoy = Inventory(productName=productName, quantity=quantity,price=price)
    inventoy.save()

    return redirect("/staff-dashboard")

def addrec(request):
    x=request.POST['productName']
    y=request.POST['notificationContent']
    z=request.POST['quantity']
    i=request.POST['barcode']
    notification = SupplierNotification(productName=x,notificationContent=y,quantity=z,barcode=i)
    notification.save()

    allbarcode = AllBarcode(barcode=i)
    allbarcode.save()

    return redirect("/manager-dashboard")

def delete(request, id):
    notification = SupplierNotification.objects.get(id=id)
    notification.delete()
    return redirect("/manager-dashboard")

def deleteInventory(request, id):
    inventory = Inventory.objects.get(id=id)
    inventory.delete()
    return redirect("/manager-dashboard")

def deleteInventoryStaff(request, id):
    inventory = Inventory.objects.get(id=id)
    inventory.delete()
    return redirect("/staff-dashboard")

def update(request, id):
    notification = SupplierNotification.objects.get(id=id)
    return render(request, 'update-notification.html', {'notification': notification})

def updateInventory(request, id):
    inventory = Inventory.objects.get(id=id)
    return render(request, 'update-inventory.html', {'inventory': inventory})

def updateInventoryStaff(request, id):
    inventory = Inventory.objects.get(id=id)
    return render(request, 'update-inventory.html', {'inventory': inventory})

def uprec(request,id):
    x=request.POST['productName']
    y=request.POST['notificationContent']
    z=request.POST['quantity']
    i=request.POST['barcode']
    notification = SupplierNotification.objects.get(id=id)
    notification.productName=x
    notification.notificationContent=y
    notification.quantity=z
    notification.barcode=i
    notification.save()
    return redirect("/manager-dashboard")

def uprecInventory(request,id):
    x=request.POST['productName']
    z=request.POST['quantity']
    i=request.POST['price']
    inventory = Inventory.objects.get(id=id)
    inventory.productName=x
    inventory.quantity=z
    inventory.price=i
    inventory.save()
    return redirect("/manager-dashboard")

def uprecInventoryStaff(request,id):
    x=request.POST['productName']
    z=request.POST['quantity']
    i=request.POST['price']
    inventory = Inventory.objects.get(id=id)
    inventory.productName=x
    inventory.quantity=z
    inventory.price=i
    inventory.save()
    return redirect("/staff-dashboard")

def RegisterPackage(request):
    if request.method == 'POST':
        barcode = request.POST['barcode']
        outboundDate = date.today()
        outboundTime = datetime.now().time()
        packagelog = PackageLog(barcode=barcode,outboundDate=outboundDate,outboundTime=outboundTime)
        packagelog.save()

        allbarcode = AllBarcode(barcode=barcode)
        allbarcode.save()

        # Redirect to a success page or any other appropriate page
        return redirect('/staff-dashboard')
    return redirect('/staff-dashboard')