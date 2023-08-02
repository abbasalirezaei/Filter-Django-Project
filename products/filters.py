from . models import Product
import django_filters
from django_filters.filters import RangeFilter

# Creating product filters
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label="Search By Name:" )
    price = RangeFilter(label="Search By Price:")


    class Meta:
        model = Product
        fields = ['name', 'price']