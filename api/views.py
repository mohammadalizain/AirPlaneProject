from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from airplanes.models import airplanes
from api.serializers import ListSerializer , DetailSerializer
from .serializers import CreateSerializer
# Create your views here.

class ListView(ListAPIView):
    queryset = airplanes.objects.all()
    serializer_class = ListSerializer


class Detailview(RetrieveAPIView):
    queryset = airplanes.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class CreateView(CreateAPIView):
    serializer_class = CreateSerializer


class UpdateView(RetrieveUpdateAPIView):
    queryset = airplanes.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class DeleteView(DestroyAPIView):
    queryset = airplanes.objects.all()
    serializer_class = ListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

