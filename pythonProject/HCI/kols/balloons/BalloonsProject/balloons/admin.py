from django.contrib import admin

# Register your models here.

from .models import *

class CollaborationAdmin(admin.TabularInline):
    model = Collaboration
    extra = 1

class AirlineAdmin(admin.ModelAdmin):
    inlines = [CollaborationAdmin,]
    list_display = ("name", "year_foundation",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class PilotAdmin(admin.ModelAdmin):
    list_display = ["name", "surname",]

admin.site.register(Pilot, PilotAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Balloon)
admin.site.register(Flight)
