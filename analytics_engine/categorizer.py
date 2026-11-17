
CATEGORY_RULES = {
    "Food": ["swiggy", "zomato", "restaurant", "food", "cafe"],
    "Shopping": ["amazon", "flipkart", "myntra", "shopping"],
    "Transportation": ["uber", "ola", "rapido", "petrol", "fuel"],
    "Subscriptions": ["netflix", "spotify", "prime video", "hotstar"],
    "Entertainment": ["movie", "cinema", "bookmyshow"],
    "Utilities": ["electricity", "water bill", "broadband", "recharge"],
    "Education": ["college", "course", "udemy", "books", "tuition"]
}


def categorize_transaction(description):
    description = description.lower()

    for category, keywords in CATEGORY_RULES.items():
        for keyword in keywords:
            if keyword in description:
                return {
                    "category": category,
                    "confidence": 0.9,
                    "matched_keyword": keyword
                }

    return {
        "category": "Other",
        "confidence": 0.3,
        "matched_keyword": None
    }
