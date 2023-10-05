from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'appFour/index.html',{'text':'Hello world','number':100})
def page1(request):
    return render(request,'appFour/page1.html',{'text1':"Đây là Page 1",'number1':100})
def page2(request):
    return render(request,'appFour/page2.html',{'text2':"Đây là Page 2",'number2':50})