from django.contrib import admin
from .models import *


# Register your models here.
def _register(model, admin_class):
    admin.site.register(model, admin_class)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'gain_margin', 'price_per_unit',)
    list_filter = ('name',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone')
    list_filter = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('delivery_date', 'client', 'delivery_address', 'paid')
    list_filter = ('client', 'delivery_date', 'paid')


class PaidOptionAdmin(admin.ModelAdmin):
    list_display = ('option',)
    list_filter = ('option',)


_register(Material, MaterialAdmin)
_register(Cake, CakeAdmin)
_register(Client, ClientAdmin)
_register(Order, OrderAdmin)
_register(PaidOption, PaidOptionAdmin)
