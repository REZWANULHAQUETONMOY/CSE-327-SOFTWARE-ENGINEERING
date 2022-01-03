def productDetails(request,pk):
    product_details = product.objects.get(id=pk)  #Contains information of a particular product
    product_images = images.objects.filter(product=product.objects.get(id=pk)) #Contains information of a particular product's images
    new_review = reviewForm()
    reviews = review.objects.filter(product=product.objects.get(id=pk)).order_by('-id')

    if request.method == 'POST':
        new_review = reviewForm(request.POST)
        if new_review.is_valid():
            new_review = new_review.save(commit=False)
            new_review.product = product_details
            new_review.user = request.user
            new_review.time = datetime.datetime.now()
            new_review.save()
            return HttpResponseRedirect(product_details.get_absolute_url())

    context = {'product_details':product_details,
    'product_images':product_images,
    'new_review':new_review,
    'reviews':reviews
    }
    return render (request,'product_details.html',context)
