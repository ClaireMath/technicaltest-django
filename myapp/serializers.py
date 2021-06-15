from myapp.models import Farmer, Product, Certificate
from rest_framework import serializers

class FarmerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ["id", "name_farmer", "siret", "address"]


class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name_product", "unit", "international_codification", "farmers"]


class CertificateSerializer (serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id", "name_certificate", "type", "farmer"]
