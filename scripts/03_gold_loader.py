import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 1. Setup Connection
load_dotenv()
db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(db_url)

try:
    # 2. Load Refined Data
    df = pd.read_csv('data/silver/refined_logistics.csv')

    # 3. Create Dimensions (The Lookups)
    workers = pd.DataFrame(df['handler_name'].unique(), columns=['worker_name'])
    warehouses = pd.DataFrame(pd.concat([df['origin'], df['destination']]).unique(), columns=['location_name'])

    # 4. Upload Dimensions (If they don't exist)
    workers.to_sql('dim_workers', engine, if_exists='append', index=False)
    warehouses.to_sql('dim_warehouses', engine, if_exists='append', index=False)

    # 5. Map IDs back to the main data
    w_map = pd.read_sql('SELECT * FROM dim_workers', engine).set_index('worker_name')['worker_id'].to_dict()
    wh_map = pd.read_sql('SELECT * FROM dim_warehouses', engine).set_index('location_name')['warehouse_id'].to_dict()

    df['worker_id'] = df['handler_name'].map(w_map)
    df['warehouse_id'] = df['location'].map(wh_map)

    # 6. Prepare and Upload Fact Table
    fact_df = df[['package_id', 'tracking_number', 'weight', 'worker_id', 'warehouse_id', 'is_damaged', 'scan_reason', 'timestamp']]
    fact_df.columns = ['package_id', 'tracking_number', 'weight', 'worker_id', 'warehouse_id', 'is_damaged', 'scan_reason', 'ts']

    fact_df.to_sql('fact_scans', engine, if_exists='append', index=False)
    print("🏆 SUCCESS: 300 records successfully moved to Postgres!")

except Exception as e:
    print(f"❌ ERROR: {e}")