from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError

from FrontEnd.models import contactdb, usersignupdb
from FrontEnd.views import loginout
from MainApp.models import departmentdb,employeedb,propertydb,propertytypedb,propertyareadb,selltypedb
from  django.core.mail import send_mail,EmailMultiAlternatives
from  django.conf import  settings


# Create your views here.


def index(request):
    return render(request,"index.html")




def adddepartment(request):
    return render(request,"adddepartment.html")

def savedepartment(request):
    if request.method=='POST':
        dn=request.POST.get('dname')
        dh=request.POST.get('dhead')
        dt=request.POST.get('dtime')
        obj=departmentdb(dname=dn,dhead=dh,dtime=dt)
        obj.save()
        return redirect(adddepartment)


def displaydepartment(request):
    data=departmentdb.objects.all()
    return render(request,"displadepartment.html",{'data':data})


def editdepartment(request, dataid):
    data = departmentdb.objects.get(id=dataid)
    return render(request, "editdepartment.html", {'data': data})


def updatedepartment(request, dataid):
    if request.method == 'POST':
        dn = request.POST.get('dname')
        dh = request.POST.get('dhead')
        dt = request.POST.get('dtime')
        departmentdb.objects.filter(id=dataid).update(dname=dn,dhead=dh,dtime=dt)
        return redirect(displaydepartment)


def deletedepartment(request, dataid):
    data = departmentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydepartment)



def addemployee(request):
    data=departmentdb.objects.all()
    return render(request,"addemployee.html",{'data':data})

def saveemployee(request):
    if request.method=='POST':
        en=request.POST.get('ename')
        ea=request.POST.get('eage')
        eg=request.POST.get('egender')
        ed=request.POST.get('edepartment')
        edi=request.POST.get('ediscription')
        ew=request.POST.get('whatsaap')
        em=request.POST.get('email')
        eb=request.POST.get('enumber')
        et=request.POST.get('nationality')
        img=request.FILES['image']
        obj1=employeedb(ename=en,eage=ea,egender=eg,edepartment=ed,ediscription=edi,whatsaap=ew,email=em,enumber=eb,nationality=et,image=img)
        obj1.save()
        subject='employee sign up'
        form_email='vibgyorealestate@gmail.com'
        msg="http://127.0.0.1:8000/FrontEnd/loginout/"
        to=em
        msg=EmailMultiAlternatives(subject,msg,form_email,[to])
        msg.content_subtype='html'
        msg.send()
        return redirect(addemployee)



def displayemployee(request):
    data=employeedb.objects.all()
    return render(request,"displayemployee.html",{'data':data})


def editdemployee(request, dataid):
    data = employeedb.objects.get(id=dataid)
    edp=departmentdb.objects.all()
    return render(request, "editemployee.html", {'data': data,'dep':edp})


def updatemployee(request, dataid):
    if request.method == 'POST':
        en = request.POST.get('ename')
        ea = request.POST.get('eage')
        eg = request.POST.get('egender')
        ed = request.POST.get('edepartment')
        edi = request.POST.get('ediscription')
        ew = request.POST.get('whatsaap')
        em = request.POST.get('email')
        eb = request.POST.get('enumber')
        et = request.POST.get('nationality')
        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = employeedb.objects.get(id=dataid).image
        employeedb.objects.filter(id=dataid).update(ename=en,eage=ea,egender=eg,edepartment=ed,ediscription=edi,whatsaap=ew,email=em,enumber=eb,nationality=et,image=file)
        return redirect(displayemployee)


def deleteemployee(request, dataid):
    data = employeedb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayemployee)





def addproperty(request):
    data=employeedb.objects.all()
    data1=propertytypedb.objects.all()
    data2=propertyareadb.objects.all()
    data3=selltypedb.objects.all()
    data5=departmentdb.objects.all()
    return render(request,"addproperty.html",{'data':data,'data1':data1,'data2':data2,'data3':data3,'data5':data5})

def saveproperty(request):
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
        pee=request.POST.get('peemail')
        ped=request.POST.get('pdepartment')
        pedi=request.POST.get('pediscription')
        peimg=request.FILES['eimage']

        obj1=propertydb(pname=en,price=ea,eemployee=eg,ptype=pt,parea=pa,stype=st,pdiscription=ed,paddress=edi,proom=ew,ptoilet=em,squarfeet=eb,pimage=img,pimage1=img1,pimage2=img2,peemail=pee,pdepartment=ped,pediscription=pedi,eimage=peimg)
        obj1.save()
        return redirect(addproperty)



def displayproperty(request):
    data=propertydb.objects.all()
    return render(request,"displayproperty.html",{'data':data})


def editproperty(request, dataid):
    data = propertydb.objects.get(id=dataid)
    data1=employeedb.objects.all()
    data2=propertytypedb.objects.all()
    data3=propertyareadb.objects.all()
    data4=selltypedb.objects.all()
    data5=departmentdb.objects.all()
    return render(request, "editproperty.html", {'data': data,'data1': data1,'data2': data2,'data3': data3,'data4': data4,'data5': data5})


def updateproperty(request, dataid):
    if request.method == 'POST':
        en=request.POST.get('pname')
        ea=request.POST.get('price')
        eg=request.POST.get('eemployee')
        pt = request.POST.get('ptype')
        pa = request.POST.get('parea')
        st = request.POST.get('stype')
        ed=request.POST.get('pdiscription')
        edi=request.POST.get('paddress')
        ew=request.POST.get('proom')
        em=request.POST.get('ptoilet')
        eb=request.POST.get('squarfeet')
        pee=request.POST.get('peemail')
        ped=request.POST.get('pdepartment')
        pedi=request.POST.get('pediscription')
        try:
            img = request.FILES['pimage']
            img1 = request.FILES['pimage1']
            img2 = request.FILES['pimage2']
            peimg = request.FILES['eimage']

            fs = FileSystemStorage()
            file = fs.save(img.name, img)
            file1 = fs.save(img1.name, img1)
            file2 = fs.save(img2.name, img2)
            file3= fs.save(peimg.name, peimg)
        except MultiValueDictKeyError:
            file = propertydb.objects.get(id=dataid).pimage
            file1 = propertydb.objects.get(id=dataid).pimage1
            file2 = propertydb.objects.get(id=dataid).pimage2
            file3 = propertydb.objects.get(id=dataid).eimage
        propertydb.objects.filter(id=dataid).update(pname=en,price=ea,eemployee=eg,ptype=pt,parea=pa,stype=st,pdiscription=ed,paddress=edi,proom=ew,ptoilet=em,squarfeet=eb,pimage=file,pimage1=file1,pimage2=file2,peemail=pee,pdepartment=ped,pediscription=pedi,eimage=file3)
        return redirect(displayproperty)


def deleteproperty(request, dataid):
    data = propertydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproperty)



def admin_login(request):
    return render(request,"Login.html")




def loginpage(request):
    if request.method=='POST':
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(index)
            else:
                return redirect(admin_login)

        else:
            return redirect(admin_login)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)


def addpropertytype(request):
    return render(request,"addpropertytype.html")


def savepropertytype(request):
    if request.method=='POST':
        dn=request.POST.get('ptname')
        obj=propertytypedb(ptname=dn)
        obj.save()
        return redirect(addpropertytype)


def displaypropertytype(request):
    data=propertytypedb.objects.all()
    return render(request,"displaypropertytype.html",{'data':data})


def editpropertytype(request, dataid):
    data = propertytypedb.objects.get(id=dataid)
    return render(request, "editpropertytype.html", {'data': data})


def updatepropertytype(request, dataid):
    if request.method == 'POST':
        dn = request.POST.get('ptname')
        propertytypedb.objects.filter(id=dataid).update(ptname=dn)
        return redirect(displaypropertytype)


def deletepropertytype(request, dataid):
    data = propertytypedb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypropertytype)


def addpropertyarea(request):
    return render(request,"addpropertyarea.html")



def savepropertyarea(request):
    if request.method=='POST':
        dn=request.POST.get('paname')
        obj=propertyareadb(paname=dn)
        obj.save()
        return redirect(addpropertyarea)


def displaypropertyarea(request):
    data=propertyareadb.objects.all()
    return render(request,"displaypropertyarea.html",{'data':data})


def editpropertyarea(request, dataid):
    data = propertyareadb.objects.get(id=dataid)
    return render(request, "editpropertyarea.html", {'data': data})


def updatepropertyarea(request, dataid):
    if request.method == 'POST':
        dn = request.POST.get('paname')
        propertyareadb.objects.filter(id=dataid).update(paname=dn)
        return redirect(displaypropertyarea)


def deletepropertyarea(request, dataid):
    data = propertyareadb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypropertyarea)



def addselltype(request):
    return render(request,"addselltype.html")



def saveselltype(request):
    if request.method=='POST':
        dn=request.POST.get('slname')
        obj=selltypedb(slname=dn)
        obj.save()
        return redirect(addselltype)


def displayselltype(request):
    data=selltypedb.objects.all()
    return render(request,"displayselltype.html",{'data':data})


def editselltype(request, dataid):
    data = selltypedb.objects.get(id=dataid)
    return render(request, "editselltype.html", {'data': data})


def updateselltype(request, dataid):
    if request.method == 'POST':
        dn = request.POST.get('slname')
        selltypedb.objects.filter(id=dataid).update(slname=dn)
        return redirect(displayselltype)


def deleteselltype(request, dataid):
    data = selltypedb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayselltype)


def displaycontact(request):
    data=contactdb.objects.all()
    return render(request,"displaycontact.html",{'data':data})


def deleteenqu(request, dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontact)


def userdisplay(request):
    data=usersignupdb.objects.all()
    return render(request,"userdisplay.html",{'data':data})
