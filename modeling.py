import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

# Load the data 
df = pd.read_csv('MachineLearningRating_v3.txt', delimiter='|')  # Change delimiter if needed

# Quick look at the data
print(df.head())
print(df.info())
print(df.isnull().sum())  # Check missing values

# Example: Convert date columns to datetime if needed
# df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])

# Example: Feature Engineering
# Calculate vehicle age
df['VehicleAge'] = 2015 - df['RegistrationYear']  

# Calculate Loss Ratio
df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
df['LossRatio'] = df['LossRatio'].replace([float('inf'), -float('inf')], 0).fillna(0)

# Example: Encode categorical variables
categorical_cols = ['Gender', 'Province', 'VehicleType']  # Add more as needed
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Check the result
print(df.head())
print(df.info())

# Example: Fill missing numerical values with median
# df['TotalClaims'] = df['TotalClaims'].fillna(df['TotalClaims'].median())

# Save cleaned data for modeling
# df.to_csv('cleaned_insurance_data.csv', index=False)

# Define your target variable and features
target = 'TotalClaims'  # For claim severity prediction
features = [col for col in df.columns if col not in ['TotalClaims', 'PolicyID', 'UnderwrittenCoverID']]  # Exclude IDs and target

# Split the data (80% train, 20% test)
X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

# Remove columns with object (non-numeric) dtype except those you want to encode
non_numeric_cols = X.select_dtypes(include=['object']).columns
print("Non-numeric columns:", non_numeric_cols)
# Option 1: Drop them if not needed
X = X.drop(columns=non_numeric_cols)

# Option 2: If you need some, encode them (already handled above for categorical_cols)
# Make sure there are no empty strings or spaces
X = X.replace(r'^\s*$', np.nan, regex=True)
X = X.fillna(0)  # Or use another imputation strategy

# Now proceed with train-test split