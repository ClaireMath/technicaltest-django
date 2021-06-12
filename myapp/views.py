from myapp.models import Farmer
from myapp.serializers import FarmerSerializer
from rest_framework import viewsets


# Create your views here.
class FarmerViewSet (viewsets.ModelViewSet) :
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
