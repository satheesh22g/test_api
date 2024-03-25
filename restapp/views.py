from rest_framework import generics, permissions
from .models import GeeksModel
from .serializers import GeeksSerializer

class MessageCreateView(generics.CreateAPIView):
    queryset = GeeksModel.objects.all()
    serializer_class = GeeksSerializer
    http_method_names = ['post']

class MessageListView(generics.ListAPIView):
    queryset = GeeksModel.objects.all()
    serializer_class = GeeksSerializer
    http_method_names = ['get']