from django.contrib import admin

from .models import (
    Contact,
    ContactLink,
    About,
    ImageAbout,
    Social
)


class ImageAboutInline(admin.StackedInline):
    model = ImageAbout
    extra = 1


@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'facebook', 'create_at')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')


@admin.register(ContactLink)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
    list_display_links = ('id', 'name', 'icon')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'mini_text')
    list_display_links = ('id', 'mini_text')
    search_fields = ('text', 'mini_text')
    inlines = (ImageAboutInline,)

@admin.register(ImageAbout)
class ImageAboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'page')
    list_display_links = ('id', 'image', 'page')
    search_fields = ('page',)
    list_filter = ('page',)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'name', 'link')
    list_display_links = ('id', 'icon', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

