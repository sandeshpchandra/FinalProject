from django.contrib import admin

from MainApp.models import departmentdb,employeedb,propertydb

# Register your models here.

admin.site.register(departmentdb)
admin.site.register(employeedb)
admin.site.register(propertydb)