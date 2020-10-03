from django.contrib import admin

from notes.models.note import Note


class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'created_at', 'solved_at')
    list_display_links = ('id', 'owner', 'name')
    readonly_fields = ('created_at', 'updated_at', 'solved_at')


admin.site.register(Note, NotesAdmin)
