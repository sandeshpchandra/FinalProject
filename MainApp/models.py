from django.db import models

# Create your models here.

class departmentdb(models.Model):
    dname=models.CharField(max_length=50,null=True,blank=True)
    dhead=models.CharField(max_length=50,null=True,blank=True)
    dtime=models.CharField(max_length=50,null=True,blank=True)


class employeedb(models.Model):
    ename=models.CharField(max_length=50,null=True,blank=True)
    eage=models.CharField(max_length=50,null=True,blank=True)
    egender=models.CharField(max_length=50,null=True,blank=True)
    edepartment=models.CharField(max_length=50,null=True,blank=True)
    ediscription=models.CharField(max_length=50,null=True,blank=True)
    whatsaap=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    enumber=models.CharField(max_length=50,null=True,blank=True)
    nationality=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(upload_to='profile',blank=True,null=True)


class propertydb(models.Model):
    pname=models.CharField(max_length=50,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    eemployee=models.CharField(max_length=50,null=True,blank=True)
    ptype=models.CharField(max_length=50,null=True,blank=True)
    parea=models.CharField(max_length=50,null=True,blank=True)
    stype=models.CharField(max_length=50,null=True,blank=True)
    pdiscription=models.CharField(max_length=50,null=True,blank=True)
    paddress=models.CharField(max_length=50,null=True,blank=True)
    proom=models.CharField(max_length=50,null=True,blank=True)
    ptoilet=models.CharField(max_length=50,null=True,blank=True)
    squarfeet=models.CharField(max_length=50,null=True,blank=True)
    pimage=models.ImageField(upload_to='proprofile',blank=True,null=True)
    pimage1=models.ImageField(upload_to='proprofile',blank=True,null=True)
    pimage2=models.ImageField(upload_to='proprofile',blank=True,null=True)
    peemail=models.CharField(max_length=100,blank=True,null=True)
    pdepartment=models.CharField(max_length=100,blank=True,null=True)
    pediscription=models.CharField(max_length=100,blank=True,null=True)
    eimage=models.ImageField(upload_to='proprofile',blank=True,null=True)






class propertytypedb(models.Model):
    ptname=models.CharField(max_length=50,null=True,blank=True)

class propertyareadb(models.Model):
    paname=models.CharField(max_length=50,null=True,blank=True)


class selltypedb(models.Model):
    slname=models.CharField(max_length=50,null=True,blank=True)
