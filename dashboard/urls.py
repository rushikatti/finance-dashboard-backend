from django.urls import path
from .views import summary, category_summary

urlpatterns = [
    path('dashboard/summary', summary),
    path('dashboard/categories', category_summary),
]