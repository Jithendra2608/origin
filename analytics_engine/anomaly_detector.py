
def detect_large_transactions(transactions, historical_context):
    anomalies = []

    for transaction in transactions:
        merchant = transaction["merchant"].lower()

        previous_amounts = [
            item["amount"]
            for item in historical_context
            if item["merchant"].lower() == merchant
        ]

        if previous_amounts:
            average = sum(previous_amounts) / len(previous_amounts)

            if transaction["amount"] > average * 2.5:
                anomalies.append({
                    "transaction_id": transaction.get("transaction_id"),
                    "merchant": transaction["merchant"],
                    "amount": transaction["amount"],
                    "type": "Large Transaction",
                    "reason": f"Amount is unusually high compared to the historical average of {average:.2f}"
                })

    return anomalies


def detect_duplicates(transactions):
    anomalies = []
    seen = set()

    for transaction in transactions:
        key = (
            transaction["merchant"].lower(),
            transaction["date"],
            transaction["amount"]
        )

        if key in seen:
            anomalies.append({
                "transaction_id": transaction.get("transaction_id"),
                "merchant": transaction["merchant"],
                "amount": transaction["amount"],
                "type": "Possible Duplicate",
                "reason": "Same merchant, date and amount found more than once"
            })
        else:
            seen.add(key)

    return anomalies


def detect_category_spikes(transactions, historical_context):
    anomalies = []

    categories = set(item["category"] for item in transactions)

    for category in categories:
        previous_amounts = [
            item["amount"]
            for item in historical_context
            if item["category"] == category
        ]

        current_amounts = [
            item["amount"]
            for item in transactions
            if item["category"] == category
        ]

        if previous_amounts and current_amounts:
            average = sum(previous_amounts) / len(previous_amounts)
            current_total = sum(current_amounts)

            if current_total > average * 3:
                anomalies.append({
                    "category": category,
                    "current_total": current_total,
                    "type": "Category Spending Spike",
                    "reason": f"Current spending is unusually high compared to the historical average transaction amount of {average:.2f}"
                })

    return anomalies
