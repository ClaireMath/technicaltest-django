from myapp.models import Farmer, Product, Certificate
from myapp.serializers import FarmerSerializer, ProductSerializer, CertificateSerializer, FarmerPCSerializer
from rest_framework import viewsets
from django.http import HttpResponse


# Create and configure your views here.
class FarmerViewSet (viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CertificateViewSet(viewsets.ModelViewSet):

    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class FarmerPCViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerPCSerializer


    """
    view certificate
    def index(request):
    return HttpResponse("Hello, world. You're at the index view.")


view detail
def detail(request, farmer_id):
    return HttpResponse("You're looking at farmer %s." % farmer_id)


view products
def products(request, farmer_id):

    response = "You're looking at the products of farmer %s."
    return HttpResponse(response % farmer_id)


def certificates(request, farmer_id):
     return HttpResponse("You're looking at the certificates of farmer %s." % farmer_id)

"""