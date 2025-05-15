# plpl-python-week-7
# Iris Dataset Analysis Project

## 📌 Objective

This project demonstrates the use of **pandas**, **matplotlib**, and **seaborn** libraries to load, explore, analyze, and visualize a dataset. It is part of an assignment aimed at practicing data handling and visualization skills in Python.

## 📁 Project Structure

.
├── iris_analysis.ipynb # Jupyter Notebook version of the project
├── iris_analysis.py # Python script version of the project
└── README.md # This file



## 📊 Dataset

- **Name**: Iris Dataset  
- **Source**: Originally from the UCI Machine Learning Repository; accessed via `sklearn.datasets.load_iris()`  
- **Features**:
  - Sepal length (cm)
  - Sepal width (cm)
  - Petal length (cm)
  - Petal width (cm)
  - Species (Setosa, Versicolor, Virginica)

## 🧪 Tasks Completed

### ✅ Task 1: Load and Explore the Dataset
- Loaded the dataset using `pandas`
- Inspected structure using `.head()`, `.info()`, and `.isnull()`
- Checked and confirmed there are no missing values

### ✅ Task 2: Basic Data Analysis
- Computed statistics: mean, median, std dev via `.describe()`
- Grouped data by species and calculated mean values
- Highlighted patterns in petal and sepal measurements

### ✅ Task 3: Data Visualization
Created the following visualizations using `matplotlib` and `seaborn`:
1. **Line Chart** – Average petal length per species
2. **Bar Chart** – Average sepal width by species
3. **Histogram** – Distribution of petal length
4. **Scatter Plot** – Sepal length vs Petal length (with species hue)

## 🛠️ How to Run

### Option 1: Jupyter Notebook
Open `iris_analysis.ipynb` using Jupyter Notebook or JupyterLab and run all cells.

### Option 2: Python Script
Run the Python script using:

```bash
python iris_analysis.py


📌 Requirements
Python 3.x

pandas

matplotlib

seaborn

scikit-learn (for loading dataset, not required if using CSV)

Install missing packages using:

pip install pandas matplotlib seaborn scikit-learn
📈 Findings
Setosa species has significantly smaller petal lengths.

Petal length is a strong indicator of species class.

Virginica tends to have the longest petals and sepals.

✍️ Author
Millicent Anyango Ocheing
Software Engineering | Data Science Enthusiast



