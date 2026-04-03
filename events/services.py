from .models import FinancialEvent
from core.validators import validate_event

def create_event(user, data):
    validate_event(data)

    event = FinancialEvent.objects.create(
        amount=data["amount"],
        type=data["type"],
        category=data["category"],
        note=data.get("note", ""),
        date=data["date"],
        created_by=user
    )

    return event

from django.db.models import Q

def get_events(filters):
    queryset = FinancialEvent.objects.filter(is_deleted=False)

    search = filters.get("search")
    event_type = filters.get("type")
    category = filters.get("category")
    start_date = filters.get("from")
    end_date = filters.get("to")

    if search:
        queryset = queryset.filter(
            Q(category__icontains=search) |
            Q(note__icontains=search)
        )

    if event_type:
        queryset = queryset.filter(type=event_type)

    if category:
        queryset = queryset.filter(category=category)

    if start_date:
        queryset = queryset.filter(date__gte=start_date)

    if end_date:
        queryset = queryset.filter(date__lte=end_date)

    return queryset.order_by("-created_at")


def delete_event(event_id):
    try:
        event = FinancialEvent.objects.get(id=event_id, is_deleted=False)
    except FinancialEvent.DoesNotExist:
        raise ValueError("Event not found")

    event.is_deleted = True
    event.save()

    return {"message": "Event deleted successfully"}



def update_event(event_id, data):
    try:
        event = FinancialEvent.objects.get(id=event_id, is_deleted=False)
    except FinancialEvent.DoesNotExist:
        raise ValueError("Event not found")

    if "amount" in data:
        if data["amount"] <= 0:
            raise ValueError("Invalid amount")
        event.amount = data["amount"]

    if "type" in data:
        event.type = data["type"]

    if "category" in data:
        event.category = data["category"]

    if "note" in data:
        event.note = data["note"]

    event.save()

    return event