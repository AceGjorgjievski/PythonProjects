from django.contrib import admin

# Register your models here.
from .models import Pilot, Airways, Balloon, Airways_Pilot, Flight


class AirwaysPilotAdmin(admin.TabularInline): #sakame modelot da bide inline
    model = Airways_Pilot
    extra = 0 # kolku pri proces polinja da se prikazhat prazni


class AirwaysAdmin(admin.ModelAdmin):
    inlines = (AirwaysPilotAdmin,)
    list_display = ("name",) # shto sakame da se gleda

admin.site.register(Airways, AirwaysAdmin) # ako imame klasa kako shto nie sakame da se prikazhuva
                                            #ja naveduvame kako vtor argument

class FlightAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user: #reception
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False



admin.site.register(Flight, FlightAdmin)

class PilotAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name",)


admin.site.register(Pilot, PilotAdmin)
admin.site.register(Balloon)
