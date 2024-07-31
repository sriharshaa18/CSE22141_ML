import numpy as np

import pandas as pd

data = pd.read_excel(r"C:\Users\year3\Downloads\Lab Session Data.xlsx")

A = data[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values

C = data['Payment (Rs)'].values

A_pinv = np.linalg.pinv(A)

X = A_pinv @ C

print("Coefficients for price prediction:")

print(X)

value1 = float(input("Enter quantity of Candies (#): "))

value2 = float(input("Enter quantity of Mangoes (Kg): "))

value3 = float(input("Enter quantity of Milk Packets (#): "))

new_data = np.array([[value1, value2, value3]])

predicted_price = new_data @ X

print(f"Predicted price: {predicted_price[0]:.2f} Rs")
