import json
import random
import os
from datetime import datetime, timedelta

os.makedirs('data/bronze', exist_ok=True)

workers = [f"Worker_{i}" for i in range(1, 13)]
warehouses = [f"Warehouse_{city}" for city in ["London", "Paris", "NY", "Tokyo", "Berlin", "Sydney", "Dubai", "Rome", "Madrid", "Seoul"]]

data = []
start_date = datetime(2026, 5, 1)

for i in range(300):
    ts = start_date + timedelta(seconds=random.randint(0, 604800))
    
    # 3 AM Date Crisis logic
    dice = random.random()
    if dice < 0.05:
        ts_str = ts.strftime("%m/%d/%y %H:%M") 
    elif dice < 0.08:
        ts_str = "NULL_ERROR_TIMEOUT" 
    else:
        ts_str = ts.strftime("%Y-%m-%d %H:%M:%S")

    # 5% Realistic Damage logic
    is_damaged = "yes" if random.random() < 0.05 else "no"

    entry = {
        "package_id": str(random.randint(1000, 9999)),
        "tracking_number": f"TRK{random.randint(100000, 999999)}",
        "weight": round(random.uniform(0.5, 50.0), 2),
        "origin": random.choice(warehouses),
        "destination": random.choice(warehouses),
        "location": random.choice(warehouses),
        "handler_name": random.choice(workers),
        "timestamp": ts_str, 
        "is_damaged": is_damaged,
        "scan_reason": random.choice(["Arrival", "Departure", "Inspection", "Sorting"])
    }
    data.append(entry)

with open('data/bronze/raw_logistics_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("🧨 BRONZE: 300 messy records generated.")