import numpy as np
import pandas as pd

# Load the data
file_path = r"C:\Users\sriva\Desktop\exp1.csv"
data = pd.read_csv(file_path)

# Extract relevant columns for feature matrix and target vector
features = data[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values
payments = data['Payment (Rs)'].values

# Determine the dimensionality of the feature space
num_features = features.shape[1]
print(f"The number of features is: {num_features}")

# Determine the number of data points
num_data_points = features.shape[0]
print(f"The number of data points is: {num_data_points}")

# Calculate the rank of the feature matrix
matrix_rank = np.linalg.matrix_rank(features)
print(f"The rank of the feature matrix is: {matrix_rank}")

# Compute the pseudo-inverse of the feature matrix
features_pinv = np.linalg.pinv(features)

# Compute the coefficients for prediction
coefficients = features_pinv @ payments

print("Coefficients for price prediction:")
print(coefficients)

# Input new values for prediction
candies_qty = float(input("Enter quantity of Candies (#): "))
mangoes_qty = float(input("Enter quantity of Mangoes (Kg): "))
milk_packets_qty = float(input("Enter quantity of Milk Packets (#): "))

# Create a new data array for prediction
new_data_point = np.array([[candies_qty, mangoes_qty, milk_packets_qty]])

# Predict the price using the coefficients
predicted_payment = new_data_point @ coefficients

print(f"Predicted payment: {predicted_payment[0]:.2f} Rs")

# Add a classification column based on the payment amount
data['Classification'] = data['Payment (Rs)'].apply(lambda x: 'Rich' if x > 200 else 'Poor')

# Print only the 'Payment (Rs)' and 'Classification' columns
print("\nPayment and Classification:")
print(data[['Payment (Rs)', 'Classification']])
