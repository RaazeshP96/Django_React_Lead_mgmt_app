from .models import Lead
from rest_framework.viewsets import ModelViewSet
from .serializers import LeadSerializer


class LeadViewSet(ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
