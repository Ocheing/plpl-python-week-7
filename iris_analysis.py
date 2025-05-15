# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set seaborn style
sns.set(style="whitegrid")

# Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset from sklearn
    iris_raw = load_iris()
    
    # Convert to DataFrame
    iris = pd.DataFrame(iris_raw.data, columns=iris_raw.feature_names)
    iris['species'] = pd.Categorical.from_codes(iris_raw.target, iris_raw.target_names)

    print("Dataset loaded successfully.\n")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display the first few rows
print("First 5 rows of the dataset:")
print(iris.head())

# Check data types and missing values
print("\nData types and missing values:")
print(iris.info())
print("\nMissing values:\n", iris.isnull().sum())

# Task 2: Basic Data Analysis

# Compute basic statistics
print("\nDescriptive statistics:")
print(iris.describe())

# Group by species and calculate mean of numerical columns
grouped_means = iris.groupby('species').mean()
print("\nMean values grouped by species:")
print(grouped_means)

# Task 3: Data Visualization

# Line chart: Plot average petal length per species
plt.figure(figsize=(8, 5))
grouped_means['petal length (cm)'].plot(kind='line', marker='o', title='Average Petal Length per Species')
plt.ylabel('Petal Length (cm)')
plt.xlabel('Species')
plt.grid(True)
plt.show()

# Bar chart: Average sepal width per species
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped_means.index, y='sepal width (cm)', data=grouped_means.reset_index())
plt.title('Average Sepal Width per Species')
plt.ylabel('Sepal Width (cm)')
plt.xlabel('Species')
plt.show()

# Histogram: Distribution of petal length
plt.figure(figsize=(8, 5))
sns.histplot(iris['petal length (cm)'], bins=15, kde=True)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris)
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# Summary of Findings
print("\nFindings and Observations:")
print("- Setosa flowers generally have shorter petals and wider sepals.")
print("- Versicolor and Virginica have overlapping sepal lengths but differ in petal length.")
print("- Petal length appears to be a strong indicator of species class.")
