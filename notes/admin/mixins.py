from fsm_admin.mixins import FSMTransitionMixin


class FSMCustomTransitionMixin(FSMTransitionMixin):

    def save_model(self, request, obj, form, change):
        """
        Меняет состояние заметки. Если состояние не было изменено и не было изменений(новая заметка),
        отрабатывает штатный механизм + если не был добавлен читатель, добавляется в читатели владелец заметки.
        """
        if change:
            fsm_field, transition = self._get_requested_transition(request)
            if transition:
                self._do_transition(transition, request, obj, form, fsm_field)
                super(FSMTransitionMixin, self).save_model(request, obj, form, change)
        else:
            super(FSMCustomTransitionMixin, self).save_model(request, obj, form, change)
