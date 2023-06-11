from django.contrib import admin

from .models import Team


class TeamInline(admin.TabularInline):
    model = Team.username.through
    extra = 1
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('username__username', 'name')
    save_on_top = True
    inlines = [TeamInline, ]
    exclude = ('username', )
