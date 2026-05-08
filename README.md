# 🚚 Logistics Data Pipeline: Project Journal & Documentation

This repository contains a complete end-to-end Data Engineering pipeline. It demonstrates the ability to generate raw data, transform it for quality, and load it into a relational database using the **Medallion Architecture**.

---

## 📓 Project Build Journal
*A log of the challenges faced and solved during the build.*

### Phase 1: Environment & Git Setup
- **The Challenge:** Initialized Git at the wrong directory level, accidentally tracking the entire Windows User folder.
- **The Fix:** Performed a "Hard Reset" by deleting local `.git` directories and re-initializing specifically within the `Logistics_Pipeline` folder. 
- **The Lesson:** Always ensure the terminal is rooted in the project folder before running `git init`.

### Phase 2: The ETL Pipeline Execution
- **The Challenge:** Attempting to load data into the "Gold" layer before the "Silver" files existed.
- **The Fix:** Established a 3-step execution order:
    1. `python scripts/01_generate_bronze.py` (Raw Data Generation)
    2. `python scripts/02_silver_transform.py` (Data Cleaning/Refining)
    3. `python scripts/03_gold_loader.py` (Database Loading)

---

## 🏗️ Technical Architecture

### 1. Medallion Layers
- **Bronze:** Raw JSON scanner logs with intentional errors (corrupt dates, missing weights).
- **Silver:** Processed CSV data. Handled null values and normalized date formats using **Pandas**.
- **Gold:** Relational **Star Schema** in PostgreSQL.

### 2. Database Schema
Created three tables to ensure data integrity:
- `dim_workers`: Stores unique handler names.
- `dim_warehouses`: Stores unique locations.
- `fact_scans`: The central table tracking package IDs, tracking numbers, and weights.

### 3. Connection Management
- Utilized **SQLAlchemy** for the database engine.
- Implemented a `.env` file to store credentials securely, preventing sensitive passwords from being pushed to version control.

---

## 🚀 Final Result
The pipeline is fully operational. Running the final script successfully loads **300 cleaned records** into the PostgreSQL database, ready for analysis and reporting.

**Status:** 🏆 COMPLETE
