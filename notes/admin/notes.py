from django.contrib import admin
from django.utils import timezone

from notes.models.note import Note


class NotesAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'owner', 'name', 'created_at', 'solved_at')
    list_display_links = ('id', 'owner', 'name')
    readonly_fields = ('created_at', 'updated_at', 'solved_at')

    def save_model(self, request, obj, form, change):
        if change:
            update_fields = []
            for k, v in form.cleaned_data.items():
                if form.initial.get(k, None) is not None and form.initial[k] != form.cleaned_data[k]:
                    if k == 'owner' and form.cleaned_data[k].id == form.initial[k] or k == 'readers':
                        continue
                    else:
                        update_fields.append(k)
                    if k == 'is_done' and form.cleaned_data[k]:
                        obj.solved_at = timezone.now()
                    else:
                        obj.solved_at = None
                    obj.save()
            print(update_fields)
            obj.save(update_fields=update_fields)
        else:
            super(NotesAdmin, self).save_model(request, obj, form, change)


admin.site.register(Note, NotesAdmin)
