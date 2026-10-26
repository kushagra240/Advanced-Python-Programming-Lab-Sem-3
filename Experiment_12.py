import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# 1. Create sample customer churn dataset
data = {
    'Age': [24, 27, 22, 32, 29, 25, 100, 30],
    'MonthlyCharges': [500, 600, 520, 580, 620, 550, 6000, None],
    'Tenure': [2, 12, 6, 24, 18, 8, 36, 10],
    'Churn': ['Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

# 2. Display dataset
print("First Five Records:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nColumn Names:")
print(df.columns)

# 3. Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

for col in ['Age', 'MonthlyCharges', 'Tenure']:
    print("\nColumn:", col)
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Mode:", df[col].mode()[0])
    print("Standard Deviation:", df[col].std())
    print("Variance:", df[col].var())
    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())
    print("Quantiles:")
    print(df[col].quantile([0.25, 0.50, 0.75]))

# 4. Data Visualization

# Histogram
df['Age'].hist(bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Box Plot
sns.boxplot(y=df['MonthlyCharges'])
plt.title('Monthly Charges - Box Plot')
plt.show()

# Scatter Plot
plt.scatter(df['Tenure'], df['MonthlyCharges'])
plt.title('Tenure vs Monthly Charges')
plt.xlabel('Tenure')
plt.ylabel('Monthly Charges')
plt.show()

# Correlation Heatmap
corr = df[['Age', 'MonthlyCharges', 'Tenure']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 5. Handle Missing Data
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing numerical values with their respective means
df[['Age', 'MonthlyCharges', 'Tenure']] = (
    df[['Age', 'MonthlyCharges', 'Tenure']]
    .fillna(df[['Age', 'MonthlyCharges', 'Tenure']].mean())
)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 6. Detect Outliers Using Z-Scores
numeric_cols = ['Age', 'MonthlyCharges', 'Tenure']

z_scores = df[numeric_cols].apply(
    lambda column: zscore(column)
)

print("\nZ-Scores:")
print(z_scores)

outliers = (z_scores.abs() > 2)
print("\nOutlier Positions (True = Possible Outlier):")
print(outliers)

# 7. Cap Outliers Using Mean +/- 2 Standard Deviations
df_cleaned = df.copy()

for col in numeric_cols:
    mean = df_cleaned[col].mean()
    std = df_cleaned[col].std()

    lower_limit = mean - 2 * std
    upper_limit = mean + 2 * std

    df_cleaned[col] = df_cleaned[col].clip(
        lower=lower_limit,
        upper=upper_limit
    )

print("\nDataset After Handling Outliers:")
print(df_cleaned)

# 8. Verify Cleaned Dataset
print("\nRemaining Missing Values:")
print(df_cleaned.isnull().sum())

# 9. Save Cleaned Dataset
df_cleaned.to_csv('cleaned_customer_churn.csv', index=False)

print("\nCleaned dataset saved successfully.")