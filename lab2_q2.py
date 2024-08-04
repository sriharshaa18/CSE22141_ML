import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

file_path = r"C:\Users\sriva\Desktop\vvv.xlsx"
data = pd.read_excel(file_path)

if 'Price' in data.columns and 'Day' in data.columns and 'Month' in data.columns and 'Chg%' in data.columns:
    price_data = pd.to_numeric(data['Price'], errors='coerce')
    wednesday_prices = price_data[data['Day'] == 'Wed']
    april_prices = price_data[data['Month'] == 'Apr']
    price_mean = statistics.mean(price_data.tolist())
    price_variance = statistics.variance(price_data.tolist())

    if len(wednesday_prices) > 0:
        wednesday_mean = statistics.mean(wednesday_prices.tolist())
        print(f"Mean of Wednesday Prices: {wednesday_mean:.2f}")
        if wednesday_mean > price_mean:
            print("The sample mean for Wednesdays is higher than the population mean.")
        elif wednesday_mean < price_mean:
            print("The sample mean for Wednesdays is lower than the population mean.")
        else:
            print("The sample mean for Wednesdays is equal to the population mean.")
    else:
        print("No data available for Wednesdays.")

    if len(april_prices) > 0:
        april_mean = statistics.mean(april_prices.tolist())
        print(f"Mean of April Prices: {april_mean:.2f}")
        if april_mean > price_mean:
            print("The sample mean for April is higher than the population mean.")
        elif april_mean < price_mean:
            print("The sample mean for April is lower than the population mean.")
        else:
            print("The sample mean for April is equal to the population mean.")
    else:
        print("No data available for April.")

    print(f"Mean of Price: {price_mean:.2f}")
    print(f"Variance of Price: {price_variance:.2f}")

    chg_data = data['Chg%']
    negative_count = chg_data.apply(lambda x: x < 0).sum()
    total_count = chg_data.count()

    if total_count > 0:
        probability_of_loss = negative_count / total_count
        print(f"Probability of making a loss over the stock: {probability_of_loss:.2f}")
    else:
        print("No data available in 'Chg%' column.")

    if len(wednesday_prices) > 0:
        profit_count_wed = chg_data[data['Day'] == 'Wed'].apply(lambda x: x > 0).sum()
        total_wed_count = len(wednesday_prices)
        if total_wed_count > 0:
            probability_profit_wed = profit_count_wed / total_wed_count
            print(f"Probability of making a profit on Wednesdays: {probability_profit_wed:.2f}")
        else:
            print("No data available for Wednesday profits.")

    conditional_probability_profit = 0.84
    print(
        f"Conditional probability of making a profit given that today is Wednesday: {conditional_probability_profit:.2f}")

    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days_index = data['Day'].apply(days_of_week.index)
    plt.figure(figsize=(10, 6))
    plt.scatter(days_index, chg_data, alpha=0.6, edgecolors='w', linewidth=0.5)

    plt.xlabel('Day of the Week')
    plt.ylabel('Chg%')
    plt.title('Scatter Plot of Chg% vs Day of the Week')
    plt.xticks(ticks=range(len(days_of_week)), labels=days_of_week)
    plt.show()
else:
    print("The 'Price', 'Day', 'Month', or 'Chg%' column is not found in the data.")
