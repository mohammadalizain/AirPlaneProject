from rest_framework.generics import ListAPIView, RetrieveAPIView
from airplanes.models import airplanes
from api.serializers import ListSerializer , DetailSerializer
# Create your views here.

class ListView(ListAPIView):
    queryset = airplanes.objects.all()
    serializer_class = ListSerializer


class Detailview(RetrieveAPIView):
    queryset = airplanes.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'