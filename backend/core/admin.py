from django.contrib import admin
from .models import MarketStore, MarketProduct, MarketOrder

@admin.register(MarketStore)
class MarketStoreAdmin(admin.ModelAdmin):
    list_display = ["name", "owner_name", "email", "category", "products_count", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "owner_name", "email"]

@admin.register(MarketProduct)
class MarketProductAdmin(admin.ModelAdmin):
    list_display = ["name", "store_name", "price", "compare_price", "stock", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "store_name", "category"]

@admin.register(MarketOrder)
class MarketOrderAdmin(admin.ModelAdmin):
    list_display = ["order_number", "buyer_name", "store_name", "total", "status", "created_at"]
    list_filter = ["status", "payment"]
    search_fields = ["order_number", "buyer_name", "store_name"]
