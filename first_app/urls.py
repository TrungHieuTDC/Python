from django.urls import path,re_path
from first_app import views

urlpatterns = [
    path(r'users',views.index,name='user'),
    path(r'form',views.create_user,name='form'),

]
