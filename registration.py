def registration(request):
    userForm = userRegistration()
    profileForm = profileRegistration()

    if request.method == 'POST':
        userForm = userRegistration(request.POST)
        profileForm = profileRegistration(request.POST,request.FILES)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request,'Account was created for ' + profile.user.username)
            return redirect ('loginPage')

    else:
        print(userForm.errors, profileForm.errors)
    
    context = {
        'userForm':userForm,
        'profileForm':profileForm
    }
    return render (request,'registration.html',context)