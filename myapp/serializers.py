from myapp.models import Farmer, Product, Certificate
from rest_framework import serializers


class FarmerSerializer(serializers.ModelSerializer):
    # certif = Certificate.objects.filter(Certificate.farmer == Farmer.id)
    class Meta:
        model = Farmer
        fields = ["id", "name_farmer", "siret", "address"]
        # fields = ["id", "name_farmer", "siret", "address", "certif"]


class ProductSerializer(serializers.ModelSerializer):
    # farmers = FarmerSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name_product", "unit", "international_codification", "farmers"]


class CertificateSerializer(serializers.ModelSerializer):
    # farmer = FarmerSerializer(many=False, read_only=True)

    class Meta:
        model = Certificate
        fields = ["id", "name_certificate", "type", "farmer"]


class FarmerPCSerializer(serializers.ModelSerializer):
    certificate = serializers.StringRelatedField(many=True)
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Farmer
        # fields = ["id", "name_farmer", "siret", "address"]
        fields = ["id", "name_farmer", "siret", "address", "products", "certificate"]
