import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from scipy.stats import zscore
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import cosine_similarity

# Load the Excel file (default is the first sheet)
df = pd.read_excel(r"C:\Users\91912\Desktop\exp3.xlsx")

print("Original DataFrame:")
print(df)

# Define categorical and numeric columns
categorical_cols = ['sex', 'on thyroxine', 'query on thyroxine', 'on antithyroid medication',
                    'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 
                    'query hypothyroid', 'query hyperthyroid', 'lithium', 
                    'goitre', 'tumor', 'hypopituitary', 'psych',
                    'TSH measured', 'T3 measured', 'TT4 measured', 
                    'T4U measured', 'FTI measured', 'TBG measured', 
                    'referral source', 'Condition']

numeric_cols = ['age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI', 'TBG']

label_encoder = LabelEncoder()

# Handle categorical columns
for col in categorical_cols:
    if df[col].dtype == 'object':
        df[col].replace('?', np.nan, inplace=True)
        df[col] = df[col].astype(str)  
    if df[col].isnull().sum() > 0:
        imputer = SimpleImputer(strategy='most_frequent')
        df[[col]] = imputer.fit_transform(df[[col]])  
        df[col] = label_encoder.fit_transform(df[col])
    else:
        df[col] = label_encoder.fit_transform(df[col])

# Convert numeric columns
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  

# Impute missing numeric values using mean or median based on presence of outliers
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        if np.abs(zscore(df[col].dropna())).max() > 3: 
            median_value = df[col].median()
            df[col].fillna(median_value, inplace=True)
        else:
            mean_value = df[col].mean()
            df[col].fillna(mean_value, inplace=True)

print("DataFrame after handling missing numeric values:")
print(df)

# Display presence of missing values
print("\nPresence of missing values in each attribute:")
missing_values = df.isnull().sum()
print(missing_values)

# Identify outliers using z-score
print("\nPresence of outliers in numeric variables (using z-score method):")
outlier_counts = {}
for col in numeric_cols:
    if df[col].dtype in ['int64', 'float64']:  
        z_scores = np.abs(zscore(df[col].dropna()))
        outliers = np.where(z_scores > 3)[0]
        outlier_counts[col] = len(outliers)
        if len(outliers) > 0:
            print(f"{col}: {len(outliers)} outliers found")
        else:
            print(f"{col}: No outliers found")
    else:
        print(f"{col}: Not numeric type, skipping z-score calculation")

print()

# Calculate mean and variance for numeric variables
print("Mean and variance (or standard deviation) for numeric variables:")
mean_variance_results = {}
for col in numeric_cols:
    if df[col].dtype in ['int64', 'float64']:  
        mean = df[col].mean()
        variance = df[col].var()
        mean_variance_results[col] = (mean, variance)
        print(f"{col}: Mean = {mean}, Variance = {variance}")
    else:
        print(f"{col}: Not numeric type, skipping mean and variance calculation")

# Calculate Jaccard Coefficient and Simple Matching Coefficient
binary_attributes = ['on thyroxine', 'query on thyroxine', 'on antithyroid medication',
                     'sick', 'pregnant', 'thyroid surgery', 'I131 treatment',
                     'query hypothyroid', 'query hyperthyroid', 'lithium',
                     'goitre', 'tumor', 'hypopituitary', 'psych',
                     'TSH measured', 'T3 measured', 'TT4 measured',
                     'T4U measured', 'FTI measured', 'TBG measured']

vector1 = df.loc[0, binary_attributes].values
vector2 = df.loc[1, binary_attributes].values

jc = jaccard_score(vector1, vector2)
smc = sum(vector1 == vector2) / len(vector1)

print(f"\nJaccard Coefficient (JC): {jc}")
print(f"Simple Matching Coefficient (SMC): {smc}")

# Calculate Cosine Similarity
vector1 = df.loc[0, df.columns != 'Record ID'].values.reshape(1, -1)
vector2 = df.loc[1, df.columns != 'Record ID'].values.reshape(1, -1)
cosine_sim = cosine_similarity(vector1, vector2)
print(f"Cosine Similarity between the two documents: {cosine_sim[0][0]}")