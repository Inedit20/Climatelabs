from django.db.models import fields

from .models import Role
import django_filters



class RolesFilter(django_filters.FilterSet):
    value = django_filters.AllValuesFilter()
    class Meta:
        model = Role
        fields= ['name']


