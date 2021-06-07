from django.contrib import admin
from .models import BinanceKey, Orders, Currency

@admin.register(BinanceKey)
class BinanceKeyAdmin(admin.ModelAdmin):

    list_display = ('api', 'secret')

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('symbol', 'side', 'quantity', 'price', 'is_complete')

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):

    list_display = ('name', 'symbol', 'position')
