def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')        
        address = request.POST.get('address', '')        
        phone = request.POST.get('phone', '')
        newOrder = order(items_json=items_json, customer=request.user, address=address,phone=phone)
        newOrder.save()        
        id = order.order_id
        messages.info (request, 'Your Order is accepted !!!')               
        return render (request,'checkout.html',{'id': id})
    return render (request,'checkout.html')

@login_required(login_url='loginPage')
cmd

    return render(request,'myorders.html',context)