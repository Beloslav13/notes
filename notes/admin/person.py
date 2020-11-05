from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from notes.models import Person


class PersonCustomAdmin(admin.ModelAdmin):
    fields = ('user', 'phone', 'birthday', 'last_activity')
    list_display = ('name', 'email', 'phone', 'birthday', 'last_activity')
    list_display_links = ('name', 'email',)
    list_filter = ('birthday', 'last_activity')
    search_fields = ('id', 'user__first_name', 'user__last_name', 'user__email')
    empty_value_display = 'Не определено'
    readonly_fields = ('last_activity', )
    ordering = ('id',)

    def name(self, user):
        full_name = f'{user.first_name} {user.last_name}'
        return full_name if len(full_name) > 1 else user.email or user.username
    name.short_description = _('Name person')


class PersonInlineAdmin(admin.StackedInline):
    model = Person
    fields = ('birthday', 'phone',)


class PersonAdmin(UserAdmin):
    # todo: нужно доработать админку, перенести модель персоны выше либо в другое место.
    inlines = (PersonInlineAdmin, )
    date_hierarchy = 'date_joined'
    empty_value_display = 'Не определено'
    list_display = ('username', 'email', 'last_name', 'first_name', 'birthday', 'date_joined', 'last_login', 'is_staff')
    readonly_fields = ('birthday', 'last_login', 'date_joined')
    ordering = ('id',)

    def birthday(self, user):
        if hasattr(user, 'person'):
            return user.person.birthday
        return ''
    birthday.short_description = 'birthday'

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj=obj)
        if obj:
            fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'birthday', 'email', )
        return fieldsets


admin.site.unregister(User)
admin.site.register(User, PersonAdmin)
admin.site.register(Person, PersonCustomAdmin)
