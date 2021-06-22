from myapp.models import Farmer, Product, Certificate
from rest_framework import serializers


class FarmerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farmer
        fields = ["id", "name_farmer", "siret", "address"]


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = ["id", "name_product", "unit", "international_codification", "farmers"]
        # read_only_fields = ('farmer',)

class CertificateSerializer(serializers.ModelSerializer):
    # farmer = FarmerSerializer(many=False, read_only=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Certificate
        fields = ["id", "name_certificate", "type", "farmer"]


class FarmerPCSerializer(serializers.ModelSerializer):
    # products = serializers.StringRelatedField(many=True)
    # (displayed only the product name, not the whole object)
    # certificate = serializers.StringRelatedField(many=True)
    products = ProductSerializer(many=True)
    certificate = CertificateSerializer(many=True)

    class Meta:
        model = Farmer
        # fields = ["id", "name_farmer", "siret", "address"]
        fields = ["id", "name_farmer", "siret", "address", "products", "certificate"]

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        farmer = Farmer.objects.create(**validated_data)
        for product_data in products_data:
            Product.objects.create(farmer=farmer, **product_data)
        return farmer


class FarmerCertifTypeSerializer(serializers.ModelSerializer):
    certificate = serializers.StringRelatedField(many=True)

    class Meta:
        model = Farmer
        # fields = ["id", "name_farmer", "siret", "address"]
        fields = ["id", "name_farmer", "siret", "address", "certificate"]

