from django.http import JsonResponse

def api_docs(request):
    return JsonResponse({
        "project": "Finance Backend API",
        "status": "running",

        "endpoints": {
            "events": {
                "create": "POST /api/events",
                "list": "GET /api/events/list",
                "update": "PATCH /api/events/update/{id}",
                "delete": "DELETE /api/events/delete/{id}"
            },
            "dashboard": {
                "summary": "GET /api/dashboard/summary",
                "categories": "GET /api/dashboard/categories"
            }
        },

        "filters": {
            "search": "/api/events/list?search=food",
            "date_range": "/api/events/list?from=2025-04-01&to=2025-04-30"
        },

        "note": "Role-based access control applied (Admin, Analyst, Viewer)"
    })