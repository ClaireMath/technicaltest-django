from myapp.models import Farmer, Product, Certificate
from myapp.serializers import FarmerSerializer, ProductSerializer, CertificateSerializer
from myapp.serializers import FarmerPCSerializer, FarmerCertifTypeSerializer
from rest_framework import viewsets


# Create and configure your views here.
getFarmerId = lambda certificate: str(certificate['farmer_id'])


class FarmerViewSet (viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

    def get_queryset(self):
        certificate_type = self.request.query_params.get('certificate_type')
        if certificate_type is not None:
            certificatesValues = Certificate.objects.filter(type=certificate_type).values()
            certificates = list(certificatesValues)
            farmerIdsAsMapObject = map(getFarmerId, certificates)
            farmerIds = list(farmerIdsAsMapObject)
            self.queryset = Farmer.objects.filter(id__in=farmerIds)

        return self.queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CertificateViewSet(viewsets.ModelViewSet):

    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class FarmerPCViewSet(viewsets.ReadOnlyModelViewSet):
# class FarmerPCViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerPCSerializer


class FarmerCertifTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerCertifTypeSerializer
