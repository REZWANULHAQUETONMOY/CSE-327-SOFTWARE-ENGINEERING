def productDetails(request,pk):
    product_details = product.objects.get(id=pk)  #Contains information of a particular product
    product_images = images.objects.filter(product=product.objects.get(id=pk)) #Contains information of a particular product's images
    new_review = reviewForm()
    reviews = review.objects.filter(product=product.objects.get(id=pk)).order_by('-id')
