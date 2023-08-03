from django.contrib import admin

from .models import Location,Items

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

class ItemsAdmin(admin.ModelAdmin):
   list_display = ('item_name', 'stock_no', 'location_id',)

admin.site.register(Location,LocationAdmin)
admin.site.register(Items, ItemsAdmin)

