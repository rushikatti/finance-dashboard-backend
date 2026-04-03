import json
from django.http import JsonResponse
from core.policies import can_access
from core.responses import success, error
from .services import create_event
from .services import create_event, get_events, delete_event, update_event

from users.models import User
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def add_event(request):
    if request.method != "POST":
        return JsonResponse(error("METHOD_NOT_ALLOWED", "Only POST allowed"), status=405)

    
    user = User.objects.first()

    if not can_access(user, "CREATE_EVENT"):
        return JsonResponse(error("FORBIDDEN", "Not allowed"), status=403)

    try:
        data = json.loads(request.body)

        event = create_event(user, data)

        return JsonResponse(success({
            "id": event.id,
            "message": "Event created successfully"
        }))

    except ValueError as e:
        return JsonResponse(error("INVALID_INPUT", str(e)), status=400)

    except Exception:
        return JsonResponse(error("SERVER_ERROR", "Something went wrong"), status=500)
    

@csrf_exempt
def list_events(request):
    user = User.objects.first()

    if not can_access(user, "VIEW_EVENTS"):
        return JsonResponse(error("FORBIDDEN", "Not allowed"), status=403)

    filters = request.GET.dict()


    events = get_events(filters)

    sort = request.GET.get('sort', 'date')
    events = events.order_by(sort)

    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))

    start = (page - 1) * limit
    end = start + limit

    events = events[start:end]

    

    data = list(events.values())

    return JsonResponse(success(data))

@csrf_exempt
def remove_event(request, event_id):
    user = User.objects.first()

    if not can_access(user, "DELETE_EVENT"):
        return JsonResponse(error("FORBIDDEN", "Not allowed"), status=403)

    try:
        result = delete_event(event_id)
        return JsonResponse(success(result))

    except ValueError as e:
        return JsonResponse(error("NOT_FOUND", str(e)), status=404)
    


@csrf_exempt
def edit_event(request, event_id):
    user = User.objects.first()

    if not can_access(user, "UPDATE_EVENT"):
        return JsonResponse(error("FORBIDDEN", "Not allowed"), status=403)

    try:
        data = json.loads(request.body)
        event = update_event(event_id, data)

        return JsonResponse(success({
            "id": event.id,
            "message": "Event updated"
        }))

    except ValueError as e:
        return JsonResponse(error("INVALID_INPUT", str(e)), status=400)