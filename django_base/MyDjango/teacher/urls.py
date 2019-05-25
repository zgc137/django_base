from django.conf.urls import url
from django.urls import path
from . import views

app_name ='teacher'
urlpatterns =[

    path(r'detail/<int:year>/<int:month>/<int:day>/<int:id>/',views.detail,),
    path(r'test1/',views.test1,name="test1"),
    path(r'test/',views.test,name="test"),
    path(r'index/',views.index,),
    path(r'login01/',views.login01),
    path(r'login/',views.login),
    path(r'upload/',views.upload),
    path(r'test2/',views.test2,name='test2'),
    path(r'details/<name>',views.details,name='details'),

]