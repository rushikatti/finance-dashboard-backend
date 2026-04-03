from events.models import FinancialEvent
from django.db.models import Sum

def get_summary():
    income = FinancialEvent.objects.filter(
        type='income',
        is_deleted=False
    ).aggregate(total=Sum('amount'))['total'] or 0

    expense = FinancialEvent.objects.filter(
        type='expense',
        is_deleted=False
    ).aggregate(total=Sum('amount'))['total'] or 0

    return {
        "total_income": float(income),
        "total_expense": float(expense),
        "net_balance": float(income - expense)
    }



def get_category_totals():
    data = FinancialEvent.objects.filter(
        is_deleted=False
    ).values('category').annotate(total=Sum('amount'))

    return list(data)