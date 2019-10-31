from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect

from .models import MasterBettingSheet, Game

# Register your models here.
admin.site.site_header = 'Manage Betting Sheets'


class GameAdmin(admin.TabularInline):
    ...
    change_form_template = 'admin/game_change_form.html'
    model = Game
    exclude = ('favorite_score', 'underdog_score')

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(GameAdmin, self).get_readonly_fields(request, obj)
        if obj and obj.is_published:
            readonly_fields = readonly_fields + ('betting_sheet', 'favorite_team', 'underdog_team', 'betting_line', 'network_name', 'date_time', 'game_of_the_week')
            if obj.is_scored:
                readonly_fields = readonly_fields + ('favorite_score', 'underdog_score')
        return readonly_fields

    def has_add_permission(self, request, obj=None):
        if obj and obj.is_published:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj and obj.is_published:
            return False
        return True

    def get_exclude(self, request, obj=None):
        exclude = super(GameAdmin, self).get_exclude(request, obj)
        if obj and obj.is_published:
            exclude_list = list(exclude)
            exclude_list.remove('favorite_score')
            exclude_list.remove('underdog_score')
            exclude = tuple(exclude_list)
        return exclude


class MasterBettingSheetAdmin(admin.ModelAdmin):
    ...
    change_form_template = 'admin/mbs_change_form.html'
    inlines = [GameAdmin, ]

    def get_form(self, request, obj=None, **kwargs):
        """Override the get_form and extend the 'exclude' keyword arg"""
        if obj and obj.is_published:
            kwargs.update({
                'exclude': getattr(kwargs, 'exclude', tuple()) + ('title',),
            })
        return super(MasterBettingSheetAdmin, self).get_form(request, obj, **kwargs)

    def response_change(self, request, mbs):
        if '_publish' in request.POST:
            MasterBettingSheet.objects.filter(pk=mbs.pk).update(is_published=True)
            self.message_user(request, "Betting Sheet Published")
        if '_score' in request.POST:
            MasterBettingSheet.objects.filter(pk=mbs.pk).update(is_scored=True)
            self.message_user(request, "Betting Sheet Scored")
        return super().response_change(request, mbs)


admin.site.register(MasterBettingSheet, MasterBettingSheetAdmin)
