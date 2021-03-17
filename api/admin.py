from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'first_line_address', 'postcode')


@admin.register(MobileNumber)
class MobileNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'customer', 'user', 'mrc', 'data_allowance', 'contract_start', 'contract_end')


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('insurance_name', 'mrc', 'excess_fee')


@admin.register(SimOnlyTariffs)
class SimoOnlyTariffsAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan_type', 'data_allowance', 'mrc', 'contract_length')


@admin.register(SimOnlyOrder)
class SimoOnlyOrder(admin.ModelAdmin):
    list_display = ('id',)

