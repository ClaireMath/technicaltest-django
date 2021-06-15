from myapp.models import Farmer, Product, Certificate
from myapp.serializers import FarmerSerializer, ProductSerializer, CertificateSerializer
from rest_framework import viewsets


# Create your views here.
class FarmerViewSet (viewsets.ModelViewSet) :
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
