
from django.shortcuts import render, redirect
from .models import POS

pos_ins = POS()

def index(request):
    return render(request, 'index.html', {'products': pos_ins.products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        image = request.POST['image']  # URL 
        pos_ins.add_product(name, price, quantity, image)
        return redirect('index')
    return render(request, 'add_product.html')

def delete_product(request, name):
    if name in pos_ins.products:
        pos_ins.delete_product(name)
    return redirect('index')

def edit_product(request, name):
    product = pos_ins.products.get(name)
    if not product:
        return redirect('index')

    if request.method == 'POST':
        price = request.POST.get('price', product.price)
        quantity = request.POST.get('quantity', product.quantity)
        image = request.POST.get('image', product.image)
        pos_ins.edit_product(name, price, quantity, image)
        return redirect('index')
    
    return render(request, 'edit_product.html', {'product': product})

    
# pos/views.py
def purchase(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        quantity_str = request.POST.get('quantity')

       
        if not quantity_str or not quantity_str.isdigit():
            return render(request, 'purchase.html', {
                'error': 'Invalid quantity. Please enter a valid number.',
                'products': pos_ins.products.values(),
            })

        quantity = int(quantity_str) 

        # Check if the product exists
        if product_name not in pos_ins.products:
            return render(request, 'purchase.html', {
                'error': 'Product not found.',
                'products': pos_ins.products.values(),
            })

        product = pos_ins.products[product_name]  #
        available_stock = product.quantity  

        # Check if there is enough stock
        if quantity >= available_stock:
            return render(request, 'purchase.html', {
                'error': 'Not enough stock.',
                'products': pos_ins.products.values(),
            })

        # Record the sale
        sale_detail = pos_ins.record_sale(product_name, quantity)
        if sale_detail:
            return render(request, 'receipt.html', {'sale_detail': sale_detail}) 

    products = pos_ins.products.values()
    return render(request, 'purchase.html', {'products': products})



def history(request):
    return render(request, 'history.html', {'history': pos_ins.history})  
