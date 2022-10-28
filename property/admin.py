from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerFlatInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('flat', 'owner')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town', 'pk')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'town', 'floor', 'has_balcony',)
    raw_id_fields = ('likes',)
    inlines = [
        OwnerFlatInline,
    ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)

