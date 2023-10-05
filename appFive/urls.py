from django.urls import path,re_path
from appFive import views

app_name = "appFive"
urlpatterns = [
    re_path(r'^register',views.register,name='register'),
]
