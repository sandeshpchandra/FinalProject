from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError

from FrontEnd.models import contactdb, useremployeedb, usersignupdb, ratedb, userinterestdb, usernotificationdb
from MainApp.models import employeedb, propertydb, propertytypedb, propertyareadb, selltypedb


# Create your views here.
def home(request):
    data=employeedb.objects.all()
    data1=propertydb.objects.all()
    data2=propertytypedb.objects.all()
    data3=propertyareadb.objects.all()
    data4=usersignupdb.objects.all()
    data5=ratedb.objects.all()
    data6=selltypedb.objects.all()
    pro=usersignupdb.objects.get(uusername=request.session['uusername'])

    return render(request,"home.html",{'data':data,'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'data6':data6,'pro':pro})


def properties(request):
    data1 = propertydb.objects.all()
    data2 = selltypedb.objects.all()
    data3 = propertyareadb.objects.all()
    data4 = propertytypedb.objects.all()
    pro = usersignupdb.objects.get(uusername=request.session['uusername'])

    return render(request,"properties.html",{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'pro':pro})


def products(request,pro_name):
    data=propertydb.objects.filter(parea=pro_name)
    data2 = propertytypedb.objects.all()
    return render(request,"products.html",{'data':data,'data2':data2})



def singleproperty(request,proid):
    pro = usersignupdb.objects.get(uusername=request.session['uusername'])
    data2 = propertytypedb.objects.all()
    data6 = selltypedb.objects.all()



    data=propertydb.objects.get(id=proid)
    return render(request,"singleproperty.html",{'data':data,'pro':pro,'data2':data2,'data6':data6})

def singleagent(request,proid):
    data=employeedb.objects.get(id=proid)
    return render(request,"singleagent.html",{'data':data})

def aboutus(request):
    data=employeedb.objects.all()
    data1=propertytypedb.objects.all()
    data2=selltypedb.objects.all()
    pro = usersignupdb.objects.get(uusername=request.session['uusername'])

    return render(request,"aboutus.html",{'data':data,'data1':data1,'data2':data2,'pro':pro})


def contactus(request):
    data1=propertytypedb.objects.all()
    pro = usersignupdb.objects.get(uusername=request.session['uusername'])

    return render(request,"contactus.html",{'data1':data1,'pro':pro})

def savecontact(request):
    if request.method=='POST':
        cn=request.POST.get('cname')
        ce=request.POST.get('cemail')
        cu=request.POST.get('cnumber')
        ct=request.POST.get('cnationality')
        cs=request.POST.get('csubject')
        cm=request.POST.get('cmessage')
        obj=contactdb(cname=cn,cemail=ce,cnumber=cu,cnationality=ct,csubject=cs,cmessage=cm)
        obj.save()
        return redirect(contactus)



def rateus(request):
    pro=usersignupdb.objects.get(uusername=request.session['uusername'])
    data6=selltypedb.objects.all()
    data2=propertytypedb.objects.all()

    return render(request,"rateus.html",{'pro':pro,'data6':data6,'data2':data2})

def loginout(request):
    return render(request,"loginout.html")


def savesignup(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        ub = request.POST.get('unumber')
        ue = request.POST.get('eemail')
        uu = request.POST.get('eusername')
        up = request.POST.get('epassword')
        uc = request.POST.get('econfirmpass')

        obj1 = useremployeedb(uname=un, unumber=ub, eemail=ue,eusername=uu, epassword=up, econfirmpass=uc)
        obj1.save()
        return redirect(loginout)










def filtertype(request,pro1_name):
    dataa=propertydb.objects.filter(ptype=pro1_name)
    data3 = propertytypedb.objects.all()
    data2=selltypedb.objects.all()
    pro = usersignupdb.objects.get(uusername=request.session['uusername'])

    return render(request,"filtertype.html",{'dataa':dataa,'data3':data3,'data2':data2,'pro':pro})



def userloginout(request):
    return render(request,"userloginout.html")


def saveusersignup(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        ub = request.POST.get('unumber')
        ue = request.POST.get('uemail')
        us = request.POST.get('uusername')
        up = request.POST.get('upassword')
        uc = request.POST.get('confirmpass')


        obj1 = usersignupdb(uname=un, unumber=ub,uusername=us, uemail=ue, upassword=up, confirmpass=uc)
        obj1.save()
        return redirect(userloginout)







def userlogin(request):
    if request.method=='POST':
        na=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')




        if usersignupdb.objects.filter(uusername=na,upassword=pwd).exists():
            request.session['uusername']=na
            request.session['upassword']=pwd

            return redirect(home)
        elif useremployeedb.objects.filter(eemail=na,epassword=pwd).exists():
            request.session['eemail']=na
            request.session['epassword']=pwd
            return redirect(employeehome)
        else:
            return redirect(userloginout)
    else:
        return redirect(userloginout)







def userlogout(request):
    del request.session['uusername']
    del request.session['upassword']
    return redirect(userloginout)

def employeelogout(request):
    del request.session['eemail']
    del request.session['epassword']
    return redirect(userloginout)








def employeeupload(request):
    data = employeedb.objects.all()
    data1 = propertytypedb.objects.all()
    data2 = propertyareadb.objects.all()
    data3 = selltypedb.objects.all()
    return render(request, "employeeupload.html", {'data': data, 'data1': data1, 'data2': data2, 'data3': data3})




def saveemployeeupload(request):
    if request.method=='POST':
        en=request.POST.get('pname')
        ea=request.POST.get('price')
        eg=request.POST.get('eemployee')
        pt=request.POST.get('ptype')
        pa=request.POST.get('parea')
        st=request.POST.get('stype')
        ed=request.POST.get('pdiscription')
        edi=request.POST.get('paddress')
        ew=request.POST.get('proom')
        em=request.POST.get('ptoilet')
        eb=request.POST.get('squarfeet')
        img=request.FILES['pimage']
        img1=request.FILES['pimage1']
        img2=request.FILES['pimage2']
        obj1=propertydb(pname=en,price=ea,eemployee=eg,ptype=pt,parea=pa,stype=st,pdiscription=ed,paddress=edi,proom=ew,ptoilet=em,squarfeet=eb,pimage=img,pimage1=img1,pimage2=img2)
        obj1.save()
        return redirect(employeeupload)









def saverate(request):
    if request.method=='POST':
        ra=request.POST.get('rating')
        rm=request.POST.get('rmessage')
        ru=request.POST.get('ruser')
        obj8=ratedb(rating=ra,rmessage=rm,ruser=ru)
        obj8.save()
        return redirect(rateus)





def filtered_data(request):
    # Assuming you are getting filter parameters from the request
    field1_value = request.GET.get('field1')
    field2_value = request.GET.get('field2')

    # Filter data from the first model
    queryset_model1 = propertydb.objects.filter(stype=field1_value)

    # Filter data from the second model
    queryset_model2 = propertydb.objects.filter(parea=field2_value)

    # Combine or present the data as needed
    context = {
        'queryset_model1': queryset_model1,
        'queryset_model2': queryset_model2,
    }

    # Pass the combined data to the template
    return render(request, 'filtered_data.html', context)



def buyrent(request,pro_name):
    data=propertydb.objects.filter(stype=pro_name)
    data2 = selltypedb.objects.all()
    data3 = propertyareadb.objects.all()
    data4 = propertytypedb.objects.all()
    pro = usersignupdb.objects.get(uusername=request.session['uusername'])

    return render(request,"buyrent.html",{'data':data,'data2':data2,'data3':data3,'data4':data4,'pro':pro})




def editprofile(request):
    pro=usersignupdb.objects.get(uusername=request.session['uusername'])
    return render(request,"editprofile.html",{'pro':pro})


def updateuser(request, dataid):
    if request.method == 'POST':
        un = request.POST.get('uname')
        ub = request.POST.get('unumber')
        ue = request.POST.get('uemail')
        us = request.POST.get('uusername')
        up = request.POST.get('upassword')
        uc = request.POST.get('confirmpass')
        try:
            img=request.FILES['uimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = usersignupdb.objects.get(id=dataid).uimage
        usersignupdb.objects.filter(id=dataid).update(uname=un, unumber=ub,uemail=ue,uusername=us,  upassword=up, confirmpass=uc,uimage=file)
        return redirect(editprofile)

def saveuserinterest(request):
    if request.method == 'POST':
        un = request.POST.get('spuname')
        ub = request.POST.get('spemail')
        ue = request.POST.get('spunumber')
        us = request.POST.get('spname')
        up = request.POST.get('spaddress')
        uc = request.POST.get('spprice')
        ud = request.POST.get('speemail')
        obj=userinterestdb(spuname=un,spemail=ub,spunumber=ue,spname=us,spaddress=up,spprice=uc,speemail=ud)
        obj.save()
        responese = redirect(properties)
        return responese

def deletesaveuserinterest(request, dataid):
    data =userinterestdb.objects.filter(id=dataid)
    data.delete()
    return redirect(properties)

def saveusernotification(request):
    if request.method == 'POST':
        un = request.POST.get('unemail')
        ub = request.POST.get('ununame')
        ue = request.POST.get('unemployee')
        us = request.POST.get('unstype')
        up = request.POST.get('unuemail')
        uc = request.POST.get('ununumber')
        obj = usernotificationdb(unemail=un, ununame=ub, unemployee=ue, unstype=us, unuemail=up, ununumber=uc)
        obj.save()
        subject = 'Interest in property'
        form_email = 'vibgyorealestate@gmail.com'
        msg = f"Hello {ue}, myself {ub}. I have an interest in your property that you have kept for {us}. You can contact me through my email {up} or through my personal number {uc}."
        to = un
        email = EmailMultiAlternatives(subject, msg, form_email, [to])
        email.content_subtype = 'html'
        email.send()
        return redirect(properties)

def employeehome(request):
    data=employeedb.objects.all()
    data1=propertydb.objects.all()
    data2=propertytypedb.objects.all()
    data3=selltypedb.objects.all()
    data4=usersignupdb.objects.all()
    data5=ratedb.objects.all()
    return render(request,"employeehome.html",{'data':data,'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})



def employeebuyrent(request,pro_name):
    data=propertydb.objects.filter(stype=pro_name)
    data2 = selltypedb.objects.all()
    data3 = propertytypedb.objects.all()
    return render(request,"employeebuyrent.html",{'data':data,'data2':data2,'data3':data3})


def employeeproperties(request):
    data1 = propertydb.objects.all()
    data2 = selltypedb.objects.all()
    data3 = propertytypedb.objects.all()
    return render(request,"employeeproperties.html",{'data1':data1,'data2':data2,'data3':data3})


def employeesingleproperty(request,proid):


    data=propertydb.objects.get(id=proid)
    return render(request,"employeesingleproperty.html",{'data':data})


def employeefiltertype(request,pro1_name):
    dataa=propertydb.objects.filter(ptype=pro1_name)
    data3 = selltypedb.objects.all()
    data2 = propertytypedb.objects.all()
    return render(request,"employeefiltertype.html",{'dataa':dataa,'data3':data3,'data2':data2})

def employeeaboutus(request):
    data=employeedb.objects.all()
    data3 = selltypedb.objects.all()
    data2 = propertytypedb.objects.all()
    return render(request,"employeeaboutus.html",{'data':data,'data3':data3,'data2':data2})


def myproperties(request):
    data=propertydb.objects.filter(peemail=request.session['eemail'])
    data1 = propertydb.objects.all()
    data2 = selltypedb.objects.all()
    data3 = propertytypedb.objects.all()
    return render(request,"myproperties.html",{'data':data,'data1':data1,'data3':data3,'data2':data2})


def intrestshown(request):
    data=userinterestdb.objects.filter(speemail=request.session['eemail'])
    data2 = selltypedb.objects.all()
    data3 = propertytypedb.objects.all()
    return render(request,"intrestshown.html",{'data':data,'data3':data3,'data2':data2})

def allagents(request):
    data=employeedb.objects.all()
    return render(request,"allagents.html",{'data':data})


def deleteinterest(request, dataid):
    data = userinterestdb.objects.filter(id=dataid)
    data.delete()
    return redirect(intrestshown)
