
from datetime import datetime


def detect_recurring_payments(transactions, historical_context):
    results = []

    merchants = set(
        item["merchant"].lower()
        for item in historical_context
    )

    for merchant in merchants:
        history = [
            item for item in historical_context
            if item["merchant"].lower() == merchant
        ]

        history.sort(key=lambda x: x["date"])

        if len(history) < 2:
            continue

        # Check whether historical payment amounts are consistent
        amounts = [item["amount"] for item in history]
        average_amount = sum(amounts) / len(amounts)

        if average_amount == 0:
            continue

        variation = (max(amounts) - min(amounts)) / average_amount

        if variation > 0.20:
            continue

        dates = [
            datetime.strptime(item["date"], "%Y-%m-%d")
            for item in history
        ]

        intervals = [
            (dates[i] - dates[i - 1]).days
            for i in range(1, len(dates))
        ]

        average_interval = sum(intervals) / len(intervals)

        if 25 <= average_interval <= 35:
            frequency = "Monthly"
        elif 5 <= average_interval <= 9:
            frequency = "Weekly"
        else:
            continue

        current = [
            item for item in transactions
            if item["merchant"].lower() == merchant
        ]

        for transaction in current:
            result = {
                "merchant": transaction["merchant"],
                "frequency": frequency,
                "previous_average": round(average_amount, 2),
                "current_amount": transaction["amount"]
            }

            if transaction["amount"] > average_amount:
                result["price_increase"] = round(
                    transaction["amount"] - average_amount, 2
                )
                result["alert"] = "Recurring payment price increased"
            else:
                result["price_increase"] = 0
                result["alert"] = "Recurring payment detected"

            results.append(result)

    return results
