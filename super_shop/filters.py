from django_filters import CharFilter,BooleanFilter
import django_filters
from .models import Advertisement

class AdvFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title',lookup_expr='icontains')
    description_adv = CharFilter(field_name='description_adv',lookup_expr='icontains')
    avilable = BooleanFilter(field_name='avilable')
    class Meta:
        models = Advertisement
        fields = ['title','description_adv','avilable']