import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з CSV файлу
fixed_df = pd.read_csv('comptagevelo2011.csv', sep=',', parse_dates=['Date'], dayfirst=True, index_col='Date')

# Групування даних за місяцями
fixed_df['Month'] = fixed_df.index.month
monthly_counts = fixed_df.groupby('Month').sum()

# Визначення найбільш популярного місяця
most_popular_month = monthly_counts['Rachel / Papineau'].idxmax()
print(f"Найбільш популярний місяць у велосипедистів у 2011 році: {most_popular_month}")


monthly_counts.plot(figsize=(15, 10))
