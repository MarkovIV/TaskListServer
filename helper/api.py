from .models import Helper
from rest_framework import viewsets, permissions
from .serializers import HelperSerializer

class HelperViewSet(viewsets.ModelViewSet):
    queryset = Helper.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HelperSerializer