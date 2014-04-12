from django.contrib import admin

from .models import Artist, Country

class CountryAdmin(admin.ModelAdmin):
	list_display = ('name', 'continent')
	list_filter = ('continent',)
	ordering = ('name',)


class ArtistAdmin(admin.ModelAdmin):
	list_display = ('fullname','group_or_artist')
	list_filter = ('country','is_group')


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Country, CountryAdmin)