from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image')
    list_display_links = ('id', 'user')
    search_fields = ('user',)
    list_filter = ('user',)
