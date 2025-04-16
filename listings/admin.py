from django.contrib import admin
from .models import Property,VisitRequest,PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'type', 'price')
    list_filter = ('type', 'location')
    search_fields = ('title', 'location')
    fields = ('title', 'location', 'type', 'price', 'description', 'image')
    list_display = ('title', 'location', 'type', 'price')
    inlines = [PropertyImageInline]


admin.site.register(VisitRequest)
    
