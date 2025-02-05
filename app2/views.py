from django.shortcuts import render
from django.http import HttpResponse
from app2.models import Logintable
from app2.models import Usertable
from app2.models import Producttable
from app2.models import Carttable
from app2.models import Billtable
from django.db.models import Q



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,"kawai.html")

def gallery(request):
    return render(request,"kproducts.html")

def aboutus(request):
    return render(request,"aboutpage.html")

def staff(request):
    return render(request,"staff.html")

def userregistration(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        d = request.POST["name4"]
        e = request.POST["name5"]
        f = request.POST["name6"]
        g = request.POST["name7"]
        x = Logintable(Username=f, Password=g, Type="User")
        x.save()
        q = Usertable(Loginid=x, Firstname=a, Lastname=b, Place=c, Mobile=d, Email=e, Username=f, Password=g,
                      Type="User")
        q.save()
        return HttpResponse("Customer Registration Success")
    return render(request, "userregistration.html")


def login(request):
    if request.method == "POST":
        a = request.POST["name1"]
        b = request.POST["name2"]
        try:
            q = Usertable.objects.get(Username=a)
            if q.Password == b:
                request.session["member_id"] = q.id
                return render(request, "Welcome.html")
            else:
                return HttpResponse("Incorrect Password")
        except Usertable.DoesNotExist:
            return HttpResponse("Username not found")

    return render(request, "login1.html")




def myaccount(request):
    return render(request, "aboutpage.html")



def productregistration(request):
    if request.method == "POST":
        a = request.POST["name1"]
        d = request.FILES["name4"]
        b = request.POST["name2"]
        c = request.POST["name3"]
        q = Producttable(Productname=a, Quantity=b, Unitprice=c, Image=d)
        q.save()
        return HttpResponse("Product added")
    return render(request, "productregistration.html")


def allproductprofiledata(request):
    q = Producttable.objects.all()
    return render(request, "productalldata.html", {"allproductkey": q})


def productprofileupdate(request, id3):
    q = Producttable.objects.get(id=id3)
    if request.method == "POST":
        q.Productname = request.POST["name1"]
        q.Image = request.FILES["name4"]
        q.Quantity = request.POST["name2"]
        q.Unitprice = request.POST["name3"]
        q.save()
        return HttpResponse("Update Success")

    return render(request, "productprofile.html", {"productprofilekey": q})


def productdelete(request, id2):
    q = Producttable.objects.get(id=id2)
    q.delete()
    return HttpResponse("Product is deleted")


def userproductdata(request):
    q = Producttable.objects.all()
    return render(request, "userproductdata.html", {"userproductdatakey": q})

def data(request, id):
    a = Producttable.objects.filter(id=id).first()
    return render(request, "datapage.html", {"detailskey": a})



def usercart(request, id4, id5, id):
    Pid = id4
    Pname = id5
    Price = id

    if request.method == "POST":
        c = request.POST["name3"]
        total = int(c) * int(Price)
        q = Carttable(Productid=Pid, Productname=Pname, Quantity=c, price=total, Userid=request.session["member_id"])
        q.save()
        a = Billtable(Productid=Pid, Productname=Pname, Quantity=c, price=total, Userid=request.session["member_id"],
                      Date=datetime.date.today())
        a.save()
        # Render the success template instead of redirecting
        return render(request, "cartsuccess.html")

    return render(request, "cart.html")

def usercartdata(request):
    a = Carttable.objects.filter(Userid=request.session["member_id"])
    x=0
    if a:
        for i in a:
            p=i.price
            x=x+p
            pid=i.Productid
            q=i.Quantity
            c=i.id

        return render(request, "usercartdata.html",{"usercartdatakey":a,"sum":x,"Productid":pid,"Quantity":q,"id":c})
    else:
        return HttpResponse("Cart is empty")

def usercartdelete(request,id10):
    q=Carttable.objects.get(id=id10)
    q.delete()
    return HttpResponse("Item  deleted from the cart")


def userbilldata(request):
    a = Billtable.objects.filter(Userid=request.session["member_id"])
    x=0
    if a:
        for i in a:
            p=i.price
            x=x+p
            pid=i.Productid
            q=i.Quantity
            c=i.id
            n=i.Firstname

    #b = Usertable.objects.filter(Loginid=request.session["member_id"])
    #for i in b:
        #d = i.Firstname
        #e = i.Mobile
        #f = i.Place


        return render(request, "userbilldata.html",{"usercartdatakey":a,"sum":x,"Productid":pid,"Quantity":q,"id":c,"Date":datetime.date.today(),"Firstname":n}) #,"Firstname":d,"Mobile":e,"Place":f})
    else:
         return HttpResponse("No orders")


def userbill(request):
    return render(request, "userbilldata.html")


def userpayment(request):
    a = Carttable.objects.filter(Userid=request.session["member_id"])
    x = 0
    for i in a:
        p = i.price
        x = x + p

    return render(request,"userpayment.html",{"sum":x,"id_new":request.session["member_id"]})

def userpaymentsuccess(request):
        cart = Carttable.objects.all()
        for i in cart:
            product = Producttable.objects.filter(Productname=i.Productname)
            if product:
                for j in product:
                    q = j.Quantity
                    Producttable.objects.filter(Productname=j.Productname).update(Quantity=q - i.Quantity)
        bill = Carttable.objects.all()
        for i in bill:
            a = Producttable.objects.filter(Productname=i.Productname).update()
            # print(a)
        Carttable.objects.filter(Userid=request.session["member_id"]).delete()
        return render(request, "lastpage.html")


def userproductsearch(request):
    if request.method=="POST":
        a=request.POST["name1"]
        q=Producttable.objects.filter(Q(Productname=a))
        if not q:
            return HttpResponse("no search result")
    return render(request,"userproductdata.html",{"usersearchkey":q})


def lgout(request):
    return redirect("home")

def cnt(request):
    return render(request,"kcontact.html")