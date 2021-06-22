"""connectingfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import FarmerViewSet, ProductViewSet, CertificateViewSet
from myapp.views import FarmerPCViewSet, FarmerCertifTypeViewSet
from rest_framework import routers


router = routers.DefaultRouter()
# for this url here is the viewset to use
router.register(r"farmers", FarmerViewSet)
router.register(r"products", ProductViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"farmersPC", FarmerPCViewSet)
router.register(r"/farmers?certificate_type=un_type", FarmerViewSet)
# /<str:certificate_type>/

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    # when on /api, the router takes over
    path('api/', include(router.urls)),
    # path('test/<certificate_type>', views.certif, name='certif')
]
