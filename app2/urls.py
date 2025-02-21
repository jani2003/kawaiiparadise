from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[path("",views.home,name="home"),
             path("back",views.home,name="home"),
             path("ga",views.gallery,name="gallary"),
             path("about",views.aboutus,name="aboutus"),
             path("staff",views.staff,name="staff"),
             path("path1", views.login, name="login"),
             path("path3", views.userregistration, name="userregistration"),
             path("path21",views.myaccount,name="myaccount"),
             path("path2", views.productregistration, name="productregistration"),
             path("path7/<id3>", views.productprofileupdate, name="productprofileupdate"),
             path("path10/<id2>",views.productdelete, name="productdelete"),
             path("path12", views.allproductprofiledata,name="allproductprofiledata"),
             path("path13", views.userproductdata, name="userproductdata"),
             path("path17", views.userproductsearch, name="userproductsearch"),
             path("path15/<id4>,<id5>,<id>", views.usercart, name="usercart"),
             path("path16", views.usercartdata, name="usercartdata"),
             path("path20", views.userbilldata, name="userbilldata"),
             path("path18", views.userbill, name="userbill"),
             path("path19/<id10>", views.usercartdelete, name="usercartdelete"),
             path("path22",views.userpayment,name="userpayment"),
             path("path23",views.userpaymentsuccess,name="userpaymentsuccess"),
             path("path24/<str:id>",views.data,name="data"),
             path("cnt",views.cnt,name="cnt"),
             path("lgout",views.lgout,name="lgout"),
             path("userwelcome",views.userwelcome,name="userwelcome")]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
