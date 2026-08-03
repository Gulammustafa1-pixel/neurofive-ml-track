# Neurofive ML Track

This repository contains my weekly tasks completed as part of the **Neurofive Machine Learning Track**.

---

# Week 1 – Exploratory Data Analysis (EDA)

## Task 1: Set Up Data Science Toolkit & Explore the Dataset

### Objective
Learn the basics of Exploratory Data Analysis (EDA) using the Titanic dataset.

### Work Completed
- Installed Python and Jupyter Notebook
- Loaded the Titanic dataset using Pandas
- Explored the dataset using:
  - head()
  - info()
  - describe()
- Identified missing values
- Classified numerical and categorical features
- Wrote observations about the dataset

---

## Task 2: Data Cleaning & Visualization

### Objective
Clean the dataset and visualize important patterns.

### Work Completed
- Filled missing values using Median and Mode
- Removed the Cabin column due to excessive missing values
- Detected outliers using a Boxplot
- Created visualizations:
  - Histogram
  - Boxplot
  - Bar Chart
  - Correlation Heatmap
- Analyzed the relationship between different features and passenger survival

---

# Week 2 – Machine Learning Fundamentals

## Task 1: Predict Titanic Survival

### Objective
Build a machine learning classification model to predict passenger survival.

### Steps Performed
- Encoded categorical columns using pd.get_dummies()
- Split the dataset into training and testing sets using train_test_split()
- Trained a Logistic Regression model
- Evaluated the model using Accuracy Score
- Generated and analyzed the Confusion Matrix

### Final Result

**Model Accuracy: 81.01%**

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Git
- GitHub

---
# Week 2 - Task 2

## House Price Prediction with Linear Regression

### Objective
Build a Linear Regression model to predict house prices.

### Features Used
- MedInc
- AveRooms
- HouseAge
- AveOccup
- Latitude

### Steps
- Loaded the California Housing dataset
- Selected important features
- Split data into training and testing sets
- Trained a Linear Regression model
- Evaluated using RMSE and R² Score
- Visualized Predicted vs Actual prices using a scatter plot

### Results
- RMSE: (Update after running)
- R² Score: (Update after running)

  # Week 3 – Machine Learning Fundamentals

## Task 1: Model Evaluation & Hyperparameter Tuning

### Objective

Improve the Titanic Survival Prediction model by evaluating it with advanced metrics and optimizing its performance using hyperparameter tuning.

### Work Completed

- Revisited the Logistic Regression model built in Week 2.
- Evaluated the model using:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix
- Learned why accuracy alone can be misleading for imbalanced datasets.
- Applied **GridSearchCV** to optimize the Logistic Regression model.
- Tuned the following hyperparameters:
  - **C**
  - **solver**
- Compared the original model with the tuned model.

### Best Hyperparameters

- **C:** 1
- **Solver:** liblinear

### Cross Validation Score

**79.63%**

### Model Comparison

| Model | Accuracy |
|--------|----------|
| Original Logistic Regression | 81.01% |
| Tuned Logistic Regression | 81.01% |

### Key Learning

This task helped me understand that evaluating a machine learning model requires more than just checking its accuracy. Metrics such as Precision, Recall, and F1-Score provide deeper insight into model performance, while GridSearchCV helps automatically find better hyperparameter values to build a more reliable model.

# Week 3 – Task 2: Customer Churn Prediction

## Objective

Build machine learning models to predict customer churn and identify the key factors influencing customer retention.

### Work Completed

- Loaded the Telco Customer Churn dataset
- Performed Exploratory Data Analysis (EDA)
- Cleaned missing values
- Encoded categorical variables using LabelEncoder
- Trained two machine learning models:
  - Logistic Regression
  - Decision Tree Classifier
- Compared both models using Accuracy and Classification Report
- Identified the top 3 important features using Decision Tree feature importance
- Wrote a business summary based on the model results

### Results

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **81.69%** |
| Decision Tree | **72.53%** |

### Key Learning

This task demonstrated how different machine learning models perform on the same business problem. Logistic Regression produced better predictive performance than the Decision Tree on this dataset, while the Decision Tree helped identify the most influential features affecting customer churn.


  # Week 4 – Task 1: Build a Proper ML Pipeline with Feature Engineering

## Objective
Build a reusable Machine Learning Pipeline using scikit-learn.

## Dataset
Titanic Dataset

## Tasks Completed
- Loaded the Titanic dataset
- Created two engineered features:
  - FamilySize
  - IsAlone
- Applied StandardScaler to numerical columns
- Applied OneHotEncoder to categorical columns
- Used ColumnTransformer for preprocessing
- Combined preprocessing and Logistic Regression into a single Pipeline
- Evaluated the model
- Saved the trained pipeline using Joblib

## Results

| Model | Accuracy |
|--------|----------|
| Logistic Regression Pipeline | **79.89%** |

## Saved Model

titanic_pipeline.pkl

## Libraries Used

- Pandas
- Scikit-learn
- Joblib

# Week 4 – Task 2: Ensemble Learning

## Models Trained

- Logistic Regression
- Random Forest
- XGBoost

## Dataset

Titanic Dataset

## Feature Engineering

- FamilySize
- IsAlone

## Comparison

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 79.89% |
| Random Forest | (Update after running) |
| XGBoost | (Update after running) |

## Libraries

- Pandas
- Scikit-learn
- XGBoost
- Matplotlib

## Key Learning

Random Forest uses bagging, while XGBoost uses boosting. Both are ensemble learning methods, but XGBoost typically achieves better predictive performance by correcting previous errors iteratively.

# Week 5 – Task 1: Handling Imbalanced & Messy Real-World Data

## Dataset
Credit Card Fraud Detection

## Objective
Learn how to handle highly imbalanced datasets using SMOTE.

## Work Completed
- Loaded the Credit Card Fraud Detection dataset
- Checked class distribution
- Visualized the imbalance using a bar chart
- Trained Logistic Regression before balancing
- Applied SMOTE to balance the training data
- Retrained the model
- Compared Precision, Recall, and F1-score before and after SMOTE

## Libraries Used
- Pandas
- Matplotlib
- Scikit-learn
- Imbalanced-learn

## Conclusion
Accuracy alone is not enough for imbalanced datasets. Precision, Recall, and F1-score provide a much better evaluation of fraud detection performance. SMOTE improves the model by creating synthetic samples for the minority class, helping the classifier detect fraudulent transactions more effectively.

## Repository

This repository will be updated every week as I continue completing the Neurofive ML Track.
