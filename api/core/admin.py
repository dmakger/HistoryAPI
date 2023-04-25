from django.contrib import admin

from .models import Person, Type, Event


class TypeAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Type, TypeAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Event, EventAdmin)
