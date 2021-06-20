from django.contrib import admin
from myapp.models import Farmer, Product, Certificate
# Register your models here.


class FarmerAdmin (admin.ModelAdmin):
    pass


admin.site.register(Farmer, FarmerAdmin)


class ProductAdmin (admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class CertificateAdmin (admin.ModelAdmin):
    pass


admin.site.register(Certificate, CertificateAdmin)
