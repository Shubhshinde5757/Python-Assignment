# ============================================================
# Deep Learning Assignment
# Loan Default Prediction using Multi-Layer Perceptron
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

# ============================================================
# 1. Load and Understand Dataset
# ============================================================

file_name = "Loan_Default.csv"

df = pd.read_csv(file_name)

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nStatistical Summary:")
print(df.describe(include="all"))

# ============================================================
# 2. Missing Values
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

# ============================================================
# 3. Check Target Class Balance
# ============================================================

print("\n" + "=" * 60)
print("TARGET CLASS DISTRIBUTION")
print("=" * 60)

print(df["Default"].value_counts())

print("\nTarget Percentage:")
print(df["Default"].value_counts(normalize=True) * 100)

# Plot class distribution
plt.figure(figsize=(6, 4))
df["Default"].value_counts().sort_index().plot(kind="bar")
plt.title("Default Class Distribution")
plt.xlabel("Default")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================================================
# 4. Separate X and Y
# ============================================================

X = df.drop("Default", axis=1)
y = df["Default"]

print("\n" + "=" * 60)
print("FEATURES AND TARGET")
print("=" * 60)

print("X Shape:", X.shape)
print("Y Shape:", y.shape)

# ============================================================
# 5. Identify Numerical and Categorical Columns
# ============================================================

numeric_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

print("\nNumerical Features:")
print(numeric_features)

print("\nCategorical Features:")
print(categorical_features)

# ============================================================
# 6. Train-Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n" + "=" * 60)
print("TRAIN TEST SPLIT")
print("=" * 60)

print("Training Data:", X_train.shape)
print("Testing Data :", X_test.shape)

# ============================================================
# 7. Preprocessing
# ============================================================

# Numerical columns:
# Missing values -> median
# Scaling -> StandardScaler

numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)

# Categorical columns:
# Missing values -> most frequent
# Encoding -> One Hot Encoding

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(
            handle_unknown="ignore",
            sparse_output=False
        ))
    ]
)

# Combine preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# ============================================================
# 8. Create MLP Classifier
# ============================================================

mlp = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

# Complete Pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", mlp)
    ]
)

# ============================================================
# 9. Train Model
# ============================================================

print("\n" + "=" * 60)
print("TRAINING MODEL")
print("=" * 60)

model.fit(X_train, y_train)

print("Model Training Completed Successfully!")

# ============================================================
# 10. Prediction
# ============================================================

y_pred = model.predict(X_test)

# ============================================================
# 11. Accuracy
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL ACCURACY")
print("=" * 60)

print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")

# ============================================================
# 12. Confusion Matrix
# ============================================================

cm = confusion_matrix(y_test, y_pred)

print("\n" + "=" * 60)
print("CONFUSION MATRIX")
print("=" * 60)

print(cm)

plt.figure(figsize=(6, 5))
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.xticks([0, 1], ["Low Risk (0)", "High Risk (1)"])
plt.yticks([0, 1], ["Low Risk (0)", "High Risk (1)"])

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j],
                 ha="center",
                 va="center")

plt.tight_layout()
plt.show()

# ============================================================
# 13. Classification Report
# ============================================================

print("\n" + "=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)

print(classification_report(y_test, y_pred))

# ============================================================
# 14. Precision, Recall and F1 Score
# ============================================================

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

print("\n" + "=" * 60)
print("PERFORMANCE METRICS")
print("=" * 60)

print("Precision :", precision)
print("Recall    :", recall)
print("F1 Score  :", f1)

# ============================================================
# 15. Plot Training Loss
# ============================================================

classifier = model.named_steps["classifier"]

plt.figure(figsize=(8, 5))
plt.plot(classifier.loss_curve_)
plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.grid(True)
plt.tight_layout()
plt.show()

# ============================================================
# 16. Hyperparameter Experiment 1 - Activation
# ============================================================

print("\n" + "=" * 60)
print("EXPERIMENT 1 - ACTIVATION FUNCTION")
print("=" * 60)

activations = ["identity", "logistic", "tanh", "relu"]

activation_results = {}

for activation in activations:

    test_model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", MLPClassifier(
                hidden_layer_sizes=(32, 16),
                activation=activation,
                solver="adam",
                max_iter=1000,
                random_state=42
            ))
        ]
    )

    test_model.fit(X_train, y_train)

    prediction = test_model.predict(X_test)

    acc = accuracy_score(y_test, prediction)

    activation_results[activation] = acc

    print(
        f"Activation = {activation:10s} "
        f"Accuracy = {acc:.4f}"
    )

# ============================================================
# 17. Hyperparameter Experiment 2 - Hidden Layers
# ============================================================

print("\n" + "=" * 60)
print("EXPERIMENT 2 - HIDDEN LAYERS")
print("=" * 60)

hidden_layers = [
    (10,),
    (20, 10),
    (50, 25),
    (100, 50, 25)
]

hidden_results = {}

for layers in hidden_layers:

    test_model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", MLPClassifier(
                hidden_layer_sizes=layers,
                activation="relu",
                solver="adam",
                max_iter=1000,
                random_state=42
            ))
        ]
    )

    test_model.fit(X_train, y_train)

    prediction = test_model.predict(X_test)

    acc = accuracy_score(y_test, prediction)

    hidden_results[str(layers)] = acc

    print(
        f"Hidden Layers = {layers} "
        f"Accuracy = {acc:.4f}"
    )

# ============================================================
# 18. Hyperparameter Experiment 3 - Learning Rate
# ============================================================

print("\n" + "=" * 60)
print("EXPERIMENT 3 - LEARNING RATE")
print("=" * 60)

learning_rates = [0.001, 0.01, 0.1]

learning_results = {}

for lr in learning_rates:

    test_model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", MLPClassifier(
                hidden_layer_sizes=(32, 16),
                activation="relu",
                solver="adam",
                learning_rate_init=lr,
                max_iter=1000,
                random_state=42
            ))
        ]
    )

    test_model.fit(X_train, y_train)

    prediction = test_model.predict(X_test)

    acc = accuracy_score(y_test, prediction)

    learning_results[str(lr)] = acc

    print(
        f"Learning Rate = {lr} "
        f"Accuracy = {acc:.4f}"
    )

# ============================================================
# 19. Compare Hyperparameter Results
# ============================================================

print("\n" + "=" * 60)
print("HYPERPARAMETER EXPERIMENT RESULTS")
print("=" * 60)

print("\nActivation Results:")
for key, value in activation_results.items():
    print(f"{key:10s} : {value:.4f}")

print("\nHidden Layer Results:")
for key, value in hidden_results.items():
    print(f"{key:15s} : {value:.4f}")

print("\nLearning Rate Results:")
for key, value in learning_results.items():
    print(f"{key:10s} : {value:.4f}")

# ============================================================
# 20. Best Hyperparameters
# ============================================================

best_activation = max(
    activation_results,
    key=activation_results.get
)

best_hidden = max(
    hidden_results,
    key=hidden_results.get
)

best_learning_rate = max(
    learning_results,
    key=learning_results.get
)

print("\n" + "=" * 60)
print("BEST HYPERPARAMETERS")
print("=" * 60)

print(
    "Best Activation Function :",
    best_activation,
    "Accuracy:",
    activation_results[best_activation]
)

print(
    "Best Hidden Layers       :",
    best_hidden,
    "Accuracy:",
    hidden_results[best_hidden]
)

print(
    "Best Learning Rate       :",
    best_learning_rate,
    "Accuracy:",
    learning_results[best_learning_rate]
)

# ============================================================
# 21. Test Model on New Loan Applicant
# ============================================================

print("\n" + "=" * 60)
print("NEW LOAN APPLICANT PREDICTION")
print("=" * 60)

# Example applicant
# Change these values according to your dataset

new_applicant = pd.DataFrame({
    "Age": [35],
    "Income": [60000],
    "LoanAmount": [20000],
    "CreditScore": [720],
    "EmploymentYears": [8],
    "ExistingLoans": [1],
    "MonthlyDebt": [1500],
    "LoanTerm": [5],
    "PreviousDefault": ["No"],
    "HomeOwnership": ["Own"]
})

# Make prediction
new_prediction = model.predict(new_applicant)

# Probability
new_probability = model.predict_proba(new_applicant)

print("\nPredicted Class:", new_prediction[0])

print(
    "Probability of Low Default Risk (0):",
    new_probability[0][0]
)

print(
    "Probability of High Default Risk (1):",
    new_probability[0][1]
)

if new_prediction[0] == 0:
    print("\nResult: LOW DEFAULT RISK")
else:
    print("\nResult: HIGH DEFAULT RISK")

# ============================================================
# END
# ============================================================

print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)