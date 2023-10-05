from django.shortcuts import render,redirect
from first_app.models import User,UserProfileInfo
from . import form
# Create your views here.
#Tạo user 
def create_user(request):
    myForm = form.FormName()
    if request.method == "POST":
        myForm = form.FormName(request.POST)
        if myForm.is_valid():
            user = myForm.save()
            return redirect('/first_app/users')

    return render(request,'basic_app/form.html',{'form':myForm})

def index(request):
    list = User.objects.values()
    list_user = {'user_list': list}
    return render(request,'index.html',context=list_user)

def form_name_view(request):
    myForm = form.FormName()

    if request.method == 'POST':
        myForm = form.FormName(request.POST)
        
        if myForm.is_valid():
            print("Validation success")
            print("Name: "+myForm.cleaned_data['name'])
            print("Email: "+myForm.cleaned_data['email'])
            print("Text: "+myForm.cleaned_data['text'])
        else:
            print("zzz")

    return render(request, 'basic_app/form.html',{'form':myForm})



   
