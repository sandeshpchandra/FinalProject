from django.urls import path

from MainApp import views

urlpatterns=[

    path('index/',views.index,name="index"),




    path('addemployee/',views.addemployee,name="addemployee"),
    path('saveemployee/',views.saveemployee,name="saveemployee"),
    path('displayemployee/',views.displayemployee,name="displayemployee"),
    path('editdemployee/<int:dataid>',views.editdemployee,name="editdemployee"),
    path('updatemployee/<int:dataid>',views.updatemployee,name="updatemployee"),
    path('deleteemployee/<int:dataid>',views.deleteemployee,name="deleteemployee"),






    path('adddepartment/',views.adddepartment,name="adddepartment"),
    path('savedepartment/',views.savedepartment,name="savedepartment"),
    path('displaydepartment/',views.displaydepartment,name="displaydepartment"),
    path('editdepartment/<int:dataid>', views.editdepartment, name="editdepartment"),
    path('updatedepartment/<int:dataid>', views.updatedepartment, name="updatedepartment"),
    path('deletedepartment/<int:dataid>', views.deletedepartment, name="deletedepartment"),







    path('addproperty/',views.addproperty,name="addproperty"),
    path('saveproperty/',views.saveproperty,name="saveproperty"),
    path('displayproperty/',views.displayproperty,name="displayproperty"),
    path('editproperty/<int:dataid>', views.editproperty, name="editproperty"),
    path('updateproperty/<int:dataid>', views.updateproperty, name="updateproperty"),
    path('deleteproperty/<int:dataid>', views.deleteproperty, name="deleteproperty"),




    path('admin_login/',views.admin_login,name="admin_login"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),




    path('addpropertytype/',views.addpropertytype,name="addpropertytype"),
    path('savepropertytype/',views.savepropertytype,name="savepropertytype"),
    path('displaypropertytype/',views.displaypropertytype,name="displaypropertytype"),
    path('editpropertytype/<int:dataid>', views.editpropertytype, name="editpropertytype"),
    path('updatepropertytype/<int:dataid>', views.updatepropertytype, name="updatepropertytype"),
    path('deletepropertytype/<int:dataid>', views.deletepropertytype, name="deletepropertytype"),

    path('addpropertyarea/', views.addpropertyarea, name="addpropertyarea"),
    path('savepropertyarea/', views.savepropertyarea, name="savepropertyarea"),
    path('displaypropertyarea/', views.displaypropertyarea, name="displaypropertyarea"),
    path('editpropertyarea/<int:dataid>', views.editpropertyarea, name="editpropertyarea"),
    path('updatepropertyarea/<int:dataid>', views.updatepropertyarea, name="updatepropertyarea"),
    path('deletepropertyarea/<int:dataid>', views.deletepropertyarea, name="deletepropertyarea"),

    path('addselltype/', views.addselltype, name="addselltype"),
    path('saveselltype/', views.saveselltype, name="saveselltype"),
    path('displayselltype/', views.displayselltype, name="displayselltype"),
    path('editselltype/<int:dataid>', views.editpropertyarea, name="editselltype"),
    path('updateselltype/<int:dataid>', views.editselltype, name="updateselltype"),
    path('deleteselltype/<int:dataid>', views.deleteselltype, name="deleteselltype"),

    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deleteenqu/<int:dataid>', views.deleteenqu, name="deleteenqu"),
    path('userdisplay/', views.userdisplay, name="userdisplay"),

]