from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contactdb(models.Model):
    cname=models.CharField(max_length=50,blank=True,null=True)
    cemail=models.CharField(max_length=50,blank=True,null=True)
    cnumber=models.CharField(max_length=50,blank=True,null=True)
    cnationality=models.CharField(max_length=50,blank=True,null=True)
    csubject=models.CharField(max_length=50,blank=True,null=True)
    cmessage=models.CharField(max_length=500,blank=True,null=True)


class useremployeedb(models.Model):
    uname=models.CharField(max_length=50,blank=True,null=True,)
    unumber=models.CharField(max_length=50,blank=True,null=True)
    eemail=models.CharField(max_length=50,blank=True,null=True)
    eusername=models.CharField(max_length=50,blank=True,null=True)
    epassword=models.CharField(max_length=50,blank=True,null=True)
    econfirmpass=models.CharField(max_length=500,blank=True,null=True)


class usersignupdb(models.Model):
    uname=models.CharField(max_length=50,blank=True,null=True)
    unumber=models.CharField(max_length=50,blank=True,null=True)
    uemail=models.CharField(max_length=50,blank=True,null=True)
    uusername=models.CharField(max_length=50,blank=True,null=True,unique=True)
    upassword=models.CharField(max_length=50,blank=True,null=True)
    confirmpass=models.CharField(max_length=500,blank=True,null=True)
    uimage=models.ImageField(upload_to="user_profile",default="profile.png")


class ratedb(models.Model):
    rating=models.IntegerField(blank=True,null=True)
    rmessage=models.CharField(max_length=500,blank=True,null=True)
    ruser=models.CharField(max_length=50,blank=True,null=True)



class userinterestdb(models.Model):
    spuname=models.CharField(max_length=50,blank=True,null=True)
    spemail=models.CharField(max_length=50,blank=True,null=True)
    spunumber=models.CharField(max_length=50,blank=True,null=True)
    spname=models.CharField(max_length=50,blank=True,null=True)
    spaddress=models.CharField(max_length=50,blank=True,null=True)
    spprice=models.CharField(max_length=50,blank=True,null=True)
    speemail=models.CharField(max_length=50,blank=True,null=True)



class usernotificationdb(models.Model):
    unemail=models.CharField(max_length=50,blank=True,null=True)
    ununame=models.CharField(max_length=50,blank=True,null=True)
    unemployee=models.CharField(max_length=50,blank=True,null=True)
    unstype=models.CharField(max_length=50,blank=True,null=True)
    unuemail=models.CharField(max_length=50,blank=True,null=True)
    ununumber=models.CharField(max_length=50,blank=True,null=True)

