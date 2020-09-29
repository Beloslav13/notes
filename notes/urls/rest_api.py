from django.urls import include, path
from rest_framework import routers

from notes.views.note import NoteViewSet

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

