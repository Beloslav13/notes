from django.contrib import admin
from django.utils import timezone

from notes.admin.mixins import FSMCustomTransitionMixin
from notes.models.note import Note


class NotesAdmin(FSMCustomTransitionMixin, admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'owner', 'name', 'created_at', 'solved_at')
    list_display_links = ('id', 'owner', 'name')
    readonly_fields = ('state_name', 'created_at', 'updated_at', 'solved_at')
    exclude = ('state',)
    fsm_field = ['state', ]

    def save_model(self, request, obj, form, change):
        if change:
            update_fields = []
            for k, v in form.cleaned_data.items():
                if form.initial.get(k, None) is not None and form.initial[k] != form.cleaned_data[k]:
                    if k == 'owner' and form.cleaned_data[k].id == form.initial[k] or k == 'readers':
                        continue
                    else:
                        update_fields.append(k)
                    # Проставляем дату закрытия заметки
                    if k == 'is_done' and form.cleaned_data[k]:
                        obj.solved_at = timezone.now()
                    elif k == 'is_done' and form.initial.get(k, None) is not None and not form.cleaned_data[k]:
                        obj.solved_at = None
                    obj.save()
            obj.save(update_fields=update_fields)
            fsm_field, transition = self._get_requested_transition(request)
            if transition:
                super(NotesAdmin, self).save_model(request, obj, form, change)
        else:
            super(NotesAdmin, self).save_model(request, obj, form, change)
            # При создании заметки добавляем в читатели владельца заметки если это поле не было заполнено.
            if not obj.readers.all().exists():
                obj.readers.add(obj.owner)
                form.cleaned_data['readers'] = obj.readers.all()

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj=obj)
        if obj:
            state = fieldsets[0][1]['fields'].pop(5)
            fieldsets[0][1]['fields'].insert(1, state)
        return fieldsets


admin.site.register(Note, NotesAdmin)
