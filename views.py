def search(request):
    query = request.GET.get('query')
    if query:
        products = product.objects.filter(product_name__icontains=query)
        context = {'products':products}
        return render(request,'search.html',context)
    else:
        return redirect('homePage')

def myOrders(request):
    orders = order.objects.all().order_by('-order_id') 
    context = {'orders':orders}
    print(orders[0].items_json)



class status(models.Model):
    status = models.CharField(max_length=50,default='Order Receieved')

    def __str__(self):
        return self.status

