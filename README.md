# NYC Airbnb Data Integration & Market Analysis

## 📌 Project Overview
This project integrates and cleans NYC Airbnb listing data collected from multiple file formats (`.csv`, `.tsv`, and `.xlsx`) to build a unified dataset for market trend analysis[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span). By combining pricing, location, property metadata, and host review details, this pipeline prepares raw multi-source data for exploratory data analysis and pricing insights[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).

---

## 🛠️ Data Sources & Pipeline
The project ingests data from three distinct sources linked by `listing_id`[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span):
* **`data/airbnb_price.csv`**: Contains listing prices and neighborhood locations[span_6](start_span)[span_6](end_span).
* **`data/airbnb_room_type.xlsx`**: Excel file containing listing descriptions and room classifications (shared, private, entire homes/apartments)[span_7](start_span)[span_7](end_span).
* **`data/airbnb_last_review.tsv`**: Tab-separated file containing host names and last review dates[span_8](start_span)[span_8](end_span).

---

## ⚡ Key Features
* **Multi-Format Ingestion:** Programmatically reads and merges CSV, Excel, and TSV files into a central `pandas` DataFrame[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span).
* **Data Harmonization:** Normalizes categorical text fields (e.g., standardizing `room_type` casing)[span_11](start_span)[span_11](end_span).
* **Data Cleaning & Type Casting:** Formats raw currency values into numeric types and parses string dates into `datetime` objects[span_12](start_span)[span_12](end_span).

---

## 📂 Project Structure
```text
├── data/
│   ├── airbnb_price.csv
│   ├── airbnb_room_type.xlsx
│   └── airbnb_last_review.tsv
├── solution.py
├── README.md
└── requirements.txt
# nyc-airbnb-data-integration-
A Python-based data integration pipeline that extracts, merges, and cleans NYC Airbnb listing data across multiple file formats (.csv, .tsv, .xlsx) for market trend analysis.  
