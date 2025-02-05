import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Load the data
file_path = "sales_invoice_report_31-01-2025-12-42-56.csv"
df = pd.read_csv(file_path)

# Debug: Print column names to verify correctness
print("Columns in dataset:", df.columns)

# Ensure the date column is correctly named
date_col = 'Invoice Date'  # Change if needed
sales_col = 'Sales'  # Change if needed

# Ensure the date column is in datetime format
df[date_col] = pd.to_datetime(df[date_col])

# Drop missing values to avoid errors
df = df.dropna()

# Aggregate sales by month
df = df.groupby(df[date_col].dt.to_period('M')).sum()
df.index = df.index.to_timestamp()

# Train the model
train_data = df[sales_col] 
model = ExponentialSmoothing(train_data, trend='add', seasonal='add', seasonal_periods=12)
fit = model.fit()

# Forecast for 2025
forecast = fit.forecast(steps=12)

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(df.index, df[sales_col], label='Historical Sales')
plt.plot(pd.date_range(start=df.index[-1], periods=13, freq='M')[1:], forecast, label='Forecast 2025', linestyle='dashed')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Forecast for 2025')
plt.legend()
plt.show()

# Save predictions to CSV
forecast_df = pd.DataFrame({'Date': pd.date_range(start=df.index[-1], periods=13, freq='M')[1:], 'Predicted_Sales': forecast})
forecast_df.to_csv("sales_forecast_2025.csv", index=False)

print("Forecast saved as 'sales_forecast_2025.csv'")
