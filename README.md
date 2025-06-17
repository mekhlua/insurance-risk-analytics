# insurance-risk-analytics
"End-to-End Insurance Risk Analytics & Predictive Modeling Project"

## EDA Findings
1. Data Overview  
The dataset contains 5 rows and 52 columns.  
Key columns analyzed: TotalPremium, TotalClaims, Gender, etc.

2. Descriptive Statistics  
TotalPremium: Mean = 6.1905e+01, Median = 2.178e+00, Min = -7.825e+02, Max = 6.528e+04  
TotalClaims: Mean = 6.486e+01, Median = 0.0000e+00, Min = -1.2001e+04, Max = ___  
There is a wide range in both premiums and claims, indicating potential outliers.

3. Missing Data  
Columns with missing values:  
Bank: 145961  
AccountType: 40232  
MaritalStatus: 82  
Gender: 95364  
mmcode: 552  
VehicleType: 552  
make: 55  
Model: 552  
Cylinders: 552  
cubiccapacity: 552  
kilowatts: 552  
bodytype: 552  
NumberOfDoors: 552  
VehicleIntroDate: 552  
CustomValueEstimate: 779642  
CapitalOutstanding: 2  
NewVehicle: 153295  
WrittenOff: 641901  
Rebuilt: 641901  
Converted: 641901  
CrossBorder: 999400  
NumberOfVehiclesInFleet: 1000098  

4. Data Types  
Most columns are correctly typed as numeric or categorical.  
Some columns may need conversion (if any issues found).

5. Univariate Distributions  
TotalPremium and TotalClaims are right-skewed, with a few very high values (outliers).  
Gender distribution:  
Male: 42817  
Female: 6755  
Not specified: 940990  
NAN: 9536  

6. Bivariate Analysis  
Correlation between TotalPremium and TotalClaims:  
Scatter plot shows (describe the pattern, e.g., weak/strong/no relationship).

7. Outlier Detection  
Box plots reveal significant outliers in TotalPremium and TotalClaims.

8. Key Insights  
There are notable outliers in financial variables.  
Gender distribution is (balanced/skewed).  
Some columns have missing data that may need to be addressed.  
There is (weak/strong) correlation between premium and claims.

## Task 2: Data Version Control (DVC)
=======
 "End-to-End Insurance Risk Analytics &amp; Predictive Modeling Project"
## EDA Findings
1. Data Overview
The dataset contains 5 rows and 52 columns.
Key columns analyzed: TotalPremium, TotalClaims, Gender, etc.

2. Descriptive Statistics
TotalPremium: Mean = _6.1905e+01, Median = 2.178e+00, Min = -7.825e+02, Max = 6.528e+04
TotalClaims: Mean = 6.486e+01, Median = 0.0000e+00, Min = -1.2001e+04, Max = ___
There is a wide range in both premiums and claims, indicating potential outliers.

3. Missing Data
Columns with missing values:
 Bank                      145961
 AccountType          40232
  MaritalStatus           82
 Gender                     95364. 
 mmcode                  552
 VehicleType            552
Data Types  make            55
  Model                             552
Cylinders                            552
cubiccapacity                   552
 kilowatts                            552
 bodytype                           552
NumberOfDoors               552
VehicleIntroDate               552
 CustomValueEstimate      779642
CapitalOutstanding              2
 NewVehicle                        153295
 WrittenOff                          641901
Rebuilt                                  641901
 Converted                           641901
 CrossBorder                        999400
 NumberOfVehiclesInFleet   1000098

4. Data Types
Most columns are correctly typed as numeric or categorical.
Some columns may need conversion (if any issues found).

5.Univariate Distributions

TotalPremium and TotalClaims are right-skewed, with a few very high values (outliers).
Gender distribution:
Male:42817
Female: 6755
Not specified: 940990
NAN: 9536

6. Bivariate Analysis
Correlation between TotalPremium and TotalClaims: 
Scatter plot shows (describe the pattern, e.g., weak/strong/no relationship).

7. Outlier Detection
Box plots reveal significant outliers in TotalPremium and TotalClaims.

8. Key Insights
There are notable outliers in financial variables.
Gender distribution is (balanced/skewed).
Some columns have missing data that may need to be addressed.
There is (weak/strong) correlation between premium and claims.

### Task 2: Data Version Control (DVC)
>>>>>>> main

#### DVC Setup
- Initialized DVC in the project.
- Added main data file (MachineLearningRating_v3.txt) to DVC tracking.
- Configured local DVC remote storage (dvc_storage/).
- Pushed data to DVC remote for reproducibility and auditability.
- Committed all DVC-related changes to Git.

#### Benefits
- Ensures data versioning and reproducibility.
- Keeps large data files out of Git, improving repo performance.
- Enables easy collaboration and rollback of data versions.

---

**Next Steps:**  
- Proceed to hypothesis testing and statistical validation (Task 3).

## Task 3: Hypothesis Testing Summary

### 1. Risk Differences Across Provinces
- **Result:** Reject the null hypothesis (risk differs across provinces).
- **Business Recommendation:** Adjust premiums by province to reflect regional risk.

### 2. Risk Differences Between Zip Codes
- **Result:** Reject the null hypothesis (risk differs across zip codes).
- **Business Recommendation:** Consider zip code-level risk segmentation for more precise pricing.

### 3. Margin Differences Between Zip Codes
- **Result:** Fail to reject the null hypothesis (no significant margin difference across zip codes).
- **Business Recommendation:** No need to adjust pricing for margin at the zip code level.

### 4. Risk Differences Between Women and Men
- **Result:** Reject the null hypothesis (risk differs between Women and Men).
<<<<<<< task-3
- **Business Recommendation:** Gender may be a relevant factor for risk segmentation and pricing.
=======
- **Business Recommendation:** Gender may be a relevant factor for risk segmentation and pricing.
