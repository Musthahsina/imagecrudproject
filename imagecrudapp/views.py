import os
from django.shortcuts import render,redirect
from .models import Product

# Create your views here.
def index(request):
    return render(request,"addproduct.html")

def addproduct(request):
    if request.method == "POST":
        pname = request.POST.get('pname')
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        image = request.FILES.get('file')

        # Save product to database
        product = Product(product_name=pname, price=price, quantity=qty, image=image)
        product.save()

        return redirect('showproduct')  # Redirect to the product listing page

    return render(request, 'addproduct.html') 

def showproduct(request):
    prdts = Product.objects.all()  # Fetch all products from the database
    return render(request, 'showproduct.html', {'prdts': prdts})

def edit(request,pk):
    prdts = Product.objects.get(id=pk)
    return render(request,'edit.html', {'prdts': prdts})

def editproduct(request,pk):
    if request.method == "POST":
        prdcts = Product.objects.get(id=pk)
        prdcts.product_name = request.POST.get('pname')
        prdcts.price = request.POST.get('price')
        prdcts.quantity = request.POST.get('qty')
        if len(request.FILES)!=0:
            if len(prdcts.image)>0:
                os.remove(prdcts.image.path)
            prdcts.image = request.FILES.get('file')
        prdcts.save()  # Save updated product details
        return redirect('showproduct')  # Redirect to product list after updating
    return render(request, 'edit.html')  # Render edit page

def delete(request,pk):
    p = Product.objects.get(id=pk)
    if p.image and os.path.isfile(p.image.path):
        os.remove(p.image.path)

    p.delete()
    return redirect('showproduct')