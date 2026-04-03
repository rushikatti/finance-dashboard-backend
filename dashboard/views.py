from django.http import JsonResponse
from core.policies import can_access
from core.responses import success, error
from .services import get_summary

from users.models import User

def summary(request):
    user = User.objects.first()

    if not can_access(user, "VIEW_DASHBOARD"):
        return JsonResponse(error("FORBIDDEN", "Not allowed"), status=403)

    data = get_summary()

    return JsonResponse(success(data))

from .services import get_category_totals

def category_summary(request):
    user = User.objects.first()

    if not can_access(user, "VIEW_DASHBOARD"):
        return JsonResponse(error("FORBIDDEN", "Not allowed"), status=403)

    data = get_category_totals()

    return JsonResponse(success(data))