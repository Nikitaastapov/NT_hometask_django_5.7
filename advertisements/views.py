from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DateFromToRangeFilter, FilterSet, DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import filters
from .filters import AdvertisementFilter
 
class CustomSearchFilter(filters.SearchFilter):
    search_param = 'creator'
    
class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
 # TODO: настройте ViewSet, укажите атрибуты для кверисета,
 #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, CustomSearchFilter]
    search_fields = ['title', 'description', 'creator__id', 'status']
    ordering_fields = ['id','user','created_at']
    filterset_class = AdvertisementFilter

    
    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated()]
    #     return []
