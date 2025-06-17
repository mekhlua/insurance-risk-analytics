import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, f_oneway

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

# Exact counts for Gender
print("\nGender Counts:")
print(df['Gender'].value_counts(dropna=False))

# --- Add the following for Task 3 metrics ---

# Calculate Claim Frequency
claim_frequency = (df['TotalClaims'] > 0).mean()
print(f"Overall Claim Frequency: {claim_frequency:.2%}")

# Calculate Claim Severity (only for policies with claims)
claim_severity = df.loc[df['TotalClaims'] > 0, 'TotalClaims'].mean()
print(f"Overall Claim Severity: {claim_severity:.2f}")

# Calculate Margin
df['Margin'] = df['TotalPremium'] - df['TotalClaims']
print("\nMargin statistics:")
print(df['Margin'].describe())

# --- Hypothesis Testing: Risk by Province ---

province_group = df.groupby('Province').agg(
    claim_frequency=('TotalClaims', lambda x: (x > 0).mean()),
    claim_severity=('TotalClaims', lambda x: x[x > 0].mean()),
    margin_mean=('Margin', 'mean'),
    count=('TotalClaims', 'count')
)
print("\nRisk Metrics by Province:")
print(province_group)

# Create a contingency table: rows=Province, columns=Claim (Yes/No)
contingency = pd.crosstab(df['Province'], df['TotalClaims'] > 0)
chi2, p, dof, expected = chi2_contingency(contingency)

print("\nChi-squared test for claim frequency across provinces:")
print(f"Chi2 statistic: {chi2:.2f}, p-value: {p:.4f}")

if p < 0.05:
    print("Result: Reject the null hypothesis (risk differs across provinces).")
else:
    print("Result: Fail to reject the null hypothesis (no significant risk difference across provinces).")

# --- Hypothesis Testing: Risk by ZipCode ---

# Group by ZipCode and calculate metrics
zipcode_group = df.groupby('PostalCode').agg(
    claim_frequency=('TotalClaims', lambda x: (x > 0).mean()),
    claim_severity=('TotalClaims', lambda x: x[x > 0].mean()),
    margin_mean=('Margin', 'mean'),
    count=('TotalClaims', 'count')
)
print("\nRisk Metrics by ZipCode (first 10 rows):")
print(zipcode_group.head(10))

# Chi-squared test for claim frequency across zip codes
contingency_zip = pd.crosstab(df['PostalCode'], df['TotalClaims'] > 0)
chi2_zip, p_zip, dof_zip, expected_zip = chi2_contingency(contingency_zip)

print("\nChi-squared test for claim frequency across zip codes:")
print(f"Chi2 statistic: {chi2_zip:.2f}, p-value: {p_zip:.4f}")

if p_zip < 0.05:
    print("Result: Reject the null hypothesis (risk differs across zip codes).")
else:
    print("Result: Fail to reject the null hypothesis (no significant risk difference across zip codes).")

# --- ANOVA Test: Margin Differences Across Zip Codes ---

# Prepare margin data grouped by zip code (only zip codes with enough data)
zip_margin_groups = [group['Margin'].dropna().values for name, group in df.groupby('PostalCode') if len(group) > 10]

# Perform one-way ANOVA
f_stat, p_val = f_oneway(*zip_margin_groups)

print("\nANOVA test for margin differences across zip codes:")
print(f"F-statistic: {f_stat:.2f}, p-value: {p_val:.4f}")

if p_val < 0.05:
    print("Result: Reject the null hypothesis (margin differs across zip codes).")
else:
    print("Result: Fail to reject the null hypothesis (no significant margin difference across zip codes).")

# --- Hypothesis Testing: Risk by Gender ---

# Group by Gender and calculate metrics
gender_group = df.groupby('Gender').agg(
    claim_frequency=('TotalClaims', lambda x: (x > 0).mean()),
    claim_severity=('TotalClaims', lambda x: x[x > 0].mean()),
    margin_mean=('Margin', 'mean'),
    count=('TotalClaims', 'count')
)
print("\nRisk Metrics by Gender:")
print(gender_group)

# Chi-squared test for claim frequency across genders
contingency_gender = pd.crosstab(df['Gender'], df['TotalClaims'] > 0)
chi2_gender, p_gender, dof_gender, expected_gender = chi2_contingency(contingency_gender)

print("\nChi-squared test for claim frequency across genders:")
print(f"Chi2 statistic: {chi2_gender:.2f}, p-value: {p_gender:.4f}")

if p_gender < 0.05:
    print("Result: Reject the null hypothesis (risk differs between Women and Men).")
else:
    print("Result: Fail to reject the null hypothesis (no significant risk difference between Women and Men).")