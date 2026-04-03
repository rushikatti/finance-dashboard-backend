from django.http import JsonResponse

def api_docs(request):
    return JsonResponse({
        "message": "Finance Backend API Documentation",

        "endpoints": {
            "Create Event": "POST /api/events",
            "List Events": "GET /api/events/list",
            "Update Event": "PATCH /api/events/update/{id}",
            "Delete Event": "DELETE /api/events/delete/{id}",

            "Dashboard Summary": "GET /api/dashboard/summary",
            "Category Summary": "GET /api/dashboard/categories"
        },

        "example_request": {
            "amount": 500,
            "type": "expense",
            "category": "food",
            "note": "lunch",
            "date": "2025-04-01"
        }
    })