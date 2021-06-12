from myapp.models import Farmer
from rest_framework import serializers

class FarmerSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Farmer
        fields = ["id", "name", "siret", "address"]