# ORIGIN – Transaction Analytics Engine

The Transaction Analytics Engine is responsible for analyzing user financial transactions and generating insights for the ORIGIN personal finance investigation system.

## Features

### 1. Transaction Categorization
- Categorizes transactions using merchant keywords.
- Supports Food, Shopping, Transportation, Subscriptions, Entertainment, Utilities and Education.
- Returns a category, confidence score and matched keyword.

### 2. Anomaly Detection
- Detects unusually large transactions.
- Identifies possible duplicate transactions.
- Detects unusual category spending spikes.

### 3. Recurring Payment Detection
- Identifies weekly and monthly recurring payments.
- Detects potential subscription price increases.
- Checks historical payment consistency.

### 4. Budget Analytics
- Calculates remaining budget.
- Calculates budget utilization percentage.
- Identifies overspending and budget warnings.

## Project Structure

```text
analytics_engine/
├── categorizer.py
├── anomaly_detector.py
├── recurring_detector.py
├── budget_analyzer.py
├── main.py
└── README.md
```

## Requirements

- Python 3.9 or later
- No external Python packages required for the current implementation.

## Running the Analytics Engine

Run the following command from the `analytics_engine` directory:

```bash
python3 main.py
```

To save the output:

```bash
python3 main.py > analytics_output.json
```

## Input Data

The current implementation reads mock financial data from the repository's `mock_data.json` file.

## Output

The engine generates structured JSON containing:

- Categorized transactions
- Detected anomalies
- Recurring payment insights
- Budget analytics

## Integration

The analytics output is intended to provide structured financial insights to the ORIGIN investigation agent.

## Current Scope

This is an initial rule-based implementation. Detection accuracy and transaction coverage can be improved as more historical and raw transaction data becomes available.