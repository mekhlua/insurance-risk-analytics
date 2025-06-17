import pandas as pd
import matplotlib.pyplot as plt

# Adjust the delimiter if your file is not comma-separated
df = pd.read_csv('MachineLearningRating_v3.txt', delimiter='|')
print(df.head())
print(df.info())

# Descriptive statistics for numerical columns
print("\nDescriptive Statistics:")
print(df.describe())

# Missing values table
missing_table = pd.DataFrame({'Column': df.columns, 'MissingValues': df.isnull().sum().values})
print("\nMissing Values Table:")
print(missing_table)

# Data types table
dtypes_table = pd.DataFrame({'Column': df.columns, 'DataType': df.dtypes.values})
print("\nData Types Table:")
print(dtypes_table)

# Histogram for TotalPremium
plt.figure(figsize=(8, 4))
df['TotalPremium'].hist(bins=50)
plt.title('Distribution of TotalPremium')
plt.xlabel('TotalPremium')
plt.ylabel('Frequency')
plt.show()

# Histogram for TotalClaims
plt.figure(figsize=(8, 4))
df['TotalClaims'].hist(bins=50)
plt.title('Distribution of TotalClaims')
plt.xlabel('TotalClaims')
plt.ylabel('Frequency')
plt.show()

# Bar plot for Gender
plt.figure(figsize=(6, 4))
df['Gender'].value_counts().plot(kind='bar')
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Scatter plot: TotalPremium vs TotalClaims
plt.figure(figsize=(8, 6))
plt.scatter(df['TotalPremium'], df['TotalClaims'], alpha=0.3)
plt.title('TotalPremium vs TotalClaims')
plt.xlabel('TotalPremium')
plt.ylabel('TotalClaims')
plt.show()

# Correlation matrix for numerical columns
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# Box plot for TotalPremium
plt.figure(figsize=(8, 4))
plt.boxplot(df['TotalPremium'].dropna(), vert=False)
plt.title('Box Plot of TotalPremium')
plt.xlabel('TotalPremium')
plt.show()

# Box plot for TotalClaims
plt.figure(figsize=(8, 4))
plt.boxplot(df['TotalClaims'].dropna(), vert=False)
plt.title('Box Plot of TotalClaims')
plt.xlabel('TotalClaims')
plt.show()