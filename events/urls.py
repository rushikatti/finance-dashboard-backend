from django.urls import path
from .views import add_event, list_events, remove_event, edit_event

urlpatterns = [
    path('events', add_event),
    path('events/list', list_events),
    path('events/delete/<int:event_id>', remove_event),
    path('events/update/<int:event_id>', edit_event),
    
]