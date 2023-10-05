from django.shortcuts import render,redirect
from appFive.models import UserInfoApp,UserProfileInfoApp
from django.contrib.auth.models import User
from . import form
# Create your views here.
def register(request):
    registered = False
    if request.method == "POST":
        user_form = form.UserInfoAppForm(data=request.POST)
        profile_form = form.UserProfileFormAppForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            userinfo = user_form.save(commit=False)
            user = User.objects.create_user(username=userinfo.user,password=userinfo.password)
            userinfo.user = user
            userinfo.save()

            profile = profile_form.save(commit=False)
            profile.user_info = userinfo

            if 'profile_pic_app' in request.FILES:
                profile.profile_pic_app = request.FILES['profile_pic_app']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = form.UserInfoAppForm()
        profile_form = form.UserProfileFormAppForm()

    return render(request, 'appFive/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})