from django.urls import include, path
from rest_framework import routers

from notes.views.note import NoteViewSet
from notes.views.person import UserViewSet

router = routers.DefaultRouter()
router.register(r'note', NoteViewSet)
router.register(r'person', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
