from django.contrib import admin
from myapp.models import Farmer
# Register your models here.

class FarmerAdmin (admin.ModelAdmin) :
    pass
admin.site.register(Farmer, FarmerAdmin)
