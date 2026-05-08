import pandas as pd
import os

os.makedirs('data/silver', exist_ok=True)

# Load the "Crude Oil"
df = pd.read_json('data/bronze/raw_logistics_data.json')

# Standardize Dates (The Fix!)
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Type Casting
df['package_id'] = df['package_id'].astype(int)
df['is_damaged'] = df['is_damaged'].map({'yes': True, 'no': False})

# Report and Save
print("-" * 30)
print(f"📊 REFINERY REPORT:")
print(f"Corrupted Dates Neutralized: {df['timestamp'].isna().sum()}")
print(f"Damaged Packages Identified: {df['is_damaged'].sum()}")
print("-" * 30)

df.to_csv('data/silver/refined_logistics.csv', index=False)
print("🥈 SILVER: Refined data saved to CSV.")