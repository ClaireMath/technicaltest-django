# we import everything we need here
from myapp.models import Farmer, Product, Certificate
from myapp.serializers import FarmerSerializer, ProductSerializer, CertificateSerializer
from myapp.serializers import FarmerPCSerializer
from rest_framework import viewsets

getFarmerId = lambda certificate: str(certificate['farmer_id'])


# Create and configure your views here.
class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

    def get_queryset(self):
        # we get the query param :
        certificate_type = self.request.query_params.get('certificate_type')
        # (if it doesn't exist, it returns the queryset line 12)
        # if it exists :
        if certificate_type is not None:
            # we get all the values of the certificates which have the type required in the param,
            certificatesValues = Certificate.objects.filter(type=certificate_type).values()
            # we make it a list
            certificates = list(certificatesValues)
            # we turn this list into a map object of farmerId's only thanks to the function getFarmerId above
            farmerIdsAsMapObject = map(getFarmerId, certificates)
            # we make it a list
            farmerIds = list(farmerIdsAsMapObject)
            # We get all the farmers who have the same id as in the list of ids present in the one which has the certificate type in param
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
