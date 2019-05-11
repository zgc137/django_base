from django.conf.urls import url
from django.urls import path
from . import views

app_name ='df_user'
urlpatterns =[
    url(r'register/',views.register),
    url(r'register_handle/',views.register_handle),
    path(r'detail/<int:year>/<int:month>/<int:day>/<int:id>/',views.detail,),
    path(r'test1/',views.test1,name="test1"),
    path(r'test/',views.test,name="test"),

]