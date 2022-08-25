from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Tag,
    Post,
    Recipe,
    Comment
)


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'image', 'category', 'create_at')
    list_display_links = ('id', 'author')
    search_fields = ('author', 'title')
    list_filter = ('author', 'tags')
    inlines = (RecipeInline,)
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    save_on_top = True
    # filter_horizontal = ('tags',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'prep_time', 'cook_time', 'post')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'serves', 'ingredients', 'directions')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'website')
    list_display_links = ('id', 'email', 'website')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email', 'website')
