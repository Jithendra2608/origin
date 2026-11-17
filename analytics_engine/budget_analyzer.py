def analyze_budgets(budgets):
    results = {}

    for category, details in budgets.items():
        limit = details["monthly_limit"]
        spent = details["current_spent"]

        remaining = limit - spent
        utilization = (spent / limit) * 100 if limit > 0 else 0

        if spent > limit:
            status = "Over Budget"
        elif utilization >= 80:
            status = "Near Budget Limit"
        else:
            status = "Within Budget"

        results[category] = {
            "monthly_limit": limit,
            "current_spent": spent,
            "remaining": remaining,
            "utilization_percentage": round(utilization, 2),
            "status": status
        }

    return results