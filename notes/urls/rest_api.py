from django.urls import include, path
from rest_framework import routers

from notes.views.note import NoteViewSet

router = routers.DefaultRouter()
router.register(r'note', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
