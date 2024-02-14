from django.urls import path

from FrontEnd import views

urlpatterns=[
    path('home/',views.home,name="home"),
    path('properties/',views.properties,name="properties"),
    path('products/<pro_name>/', views.products, name="products"),
    path('singleproperty/<int:proid>/',views.singleproperty,name="singleproperty"),
    path('singleagent/<int:proid>/',views.singleagent,name="singleagent"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('contactus/',views.contactus,name="contactus"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('rateus/',views.rateus,name="rateus"),
    path('loginout/',views.loginout,name="loginout"),
    path('savesignup/',views.savesignup,name="savesignup"),
    path('filtertype/<pro1_name>/', views.filtertype, name="filtertype"),
    path('userloginout/', views.userloginout, name="userloginout"),
    path('saveusersignup/', views.saveusersignup, name="saveusersignup"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('employeehome/', views.employeehome, name="employeehome"),
    path('intrestshown/', views.intrestshown, name="intrestshown"),
    path('employeeupload/', views.employeeupload, name="employeeupload"),
    path('saveemployeeupload/', views.saveemployeeupload, name="saveemployeeupload"),
    path('myproperties/', views.myproperties, name="myproperties"),
    path('saverate/', views.saverate, name="saverate"),
    path('filtered_data/', views.filtered_data, name='filtered_data'),
    path('buyrent/<pro_name>/', views.buyrent, name="buyrent"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('updateuser/<int:dataid>/', views.updateuser, name="updateuser"),
    path('deletesaveuserinterest/<int:dataid>/', views.deletesaveuserinterest, name="deletesaveuserinterest"),
    path('saveuserinterest/', views.saveuserinterest, name="saveuserinterest"),
    path('saveusernotification/', views.saveusernotification, name="saveusernotification"),
    path('employeebuyrent/<pro_name>/', views.employeebuyrent, name="employeebuyrent"),
    path('employeeproperties/', views.employeeproperties, name="employeeproperties"),
    path('employeesingleproperty/<int:proid>/', views.employeesingleproperty, name="employeesingleproperty"),
    path('employeefiltertype/<pro1_name>/', views.employeefiltertype, name="employeefiltertype"),
    path('employeeaboutus/', views.employeeaboutus, name="employeeaboutus"),
    path('allagents/', views.allagents, name="allagents"),
    path('deleteinterest/<int:dataid>', views.deleteinterest, name="deleteinterest"),
    path('employeelogout/', views.employeelogout, name="employeelogout"),

]