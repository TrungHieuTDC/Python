from django.urls import path, re_path
from appFour import views

app_name = "appFour"
urlpatterns = [
    re_path(r'^index/$',views.index,name='index'),
    re_path(r'^page1/$',views.page1,name='page1'),
    re_path(r'^page2/$',views.page2,name='page2')
]
