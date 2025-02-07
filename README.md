# Sales Forecasting Using Exponential Smoothing

## Overview
This project performs **sales forecasting** using **Exponential Smoothing** from the `statsmodels` library in Python. It takes historical sales data from a CSV file, processes it, and generates a **12-month forecast for 2025**.

## Features
- **Data Preprocessing**: Cleans and prepares sales data.
- **Time Series Aggregation**: Groups sales data by month.
- **Exponential Smoothing Model**: Implements **Holt-Winters Exponential Smoothing** with additive trend and seasonality.
- **12-Month Forecast**: Predicts future sales for the year 2025.
- **Visualization**: Plots historical sales and future predictions.
- **CSV Output**: Saves forecasted values in a CSV file.

## Technology Stack
- **Python** for scripting
- **Pandas** for data handling
- **Matplotlib** for visualization
- **Statsmodels** for time series forecasting

## File Structure
```
project-folder/
│── sales_forecast.py         # Main Python script
│── sales_invoice_report.csv  # Input sales data
│── sales_forecast_2025.csv   # Output forecasted sales data
```

## Installation & Usage
### **1. Install Required Libraries**
Ensure you have the required Python libraries installed:
```bash
pip install pandas matplotlib statsmodels
```

### **2. Run the Forecasting Script**
Execute the Python script to generate the forecast:
```bash
python sales_forecast.py
```

### **3. View Output**
- The script will generate a **sales forecast plot**.
- Forecasted sales data is saved in `sales_forecast_2025.csv`.

## How It Works
### **1. Load and Preprocess Data**
- Reads the sales data from `sales_invoice_report.csv`.
- Converts the **Invoice Date** column to a datetime format.
- Aggregates total sales per month.

### **2. Apply Exponential Smoothing Model**
- Uses **Holt-Winters Exponential Smoothing** with:
  - **Additive Trend**
  - **Additive Seasonality** (12-month period)
- Trains the model on historical data.

### **3. Forecast Future Sales**
- Predicts sales for the next 12 months (2025).
- Saves predictions in a CSV file.

## Visualization
The script generates a **line plot** displaying:
- **Historical Sales** (solid line)
- **Predicted Sales for 2025** (dashed line)

## Conclusion
This project provides a **data-driven approach** for sales forecasting using **time series analysis**. By leveraging **Exponential Smoothing**, it generates accurate predictions and visualizes trends for business decision-making.

---
**Author:** Harish  
**Internship:** MinervaSoft  
**Project:** Sales Forecasting System

