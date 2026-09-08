# Fraudulent Transaction Detection
# Machine Learning Assignment

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ---------------------------------------------------------
# 1. Load Dataset
# ---------------------------------------------------------

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("Dataset Loaded Successfully")
print("--------------------------------")
print("Shape:", df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

# ---------------------------------------------------------
# 2. Check Missing Values
# ---------------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# ---------------------------------------------------------
# 3. Separate Input and Target
# ---------------------------------------------------------

X = df.drop("Fraud", axis=1)
y = df["Fraud"]

print("\nInput Features:")
print(X.columns)

print("\nTarget:")
print("Fraud")

# ---------------------------------------------------------
# 4. Train-Test Split
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data :", X_test.shape)

# ---------------------------------------------------------
# 5. Create Models
# ---------------------------------------------------------

# 1. Decision Tree
decision_tree = DecisionTreeClassifier(
    random_state=42
)

# 2. Bagging Classifier
bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=100,
    random_state=42
)

# 3. Random Forest
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# 4. AdaBoost
adaboost = AdaBoostClassifier(
    n_estimators=100,
    random_state=42
)

# ---------------------------------------------------------
# 6. Voting Classifier
# ---------------------------------------------------------

voting = VotingClassifier(
    estimators=[
        ("decision_tree", DecisionTreeClassifier(random_state=42)),
        ("random_forest", RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )),
        ("adaboost", AdaBoostClassifier(
            n_estimators=100,
            random_state=42
        ))
    ],
    voting="hard"
)

# ---------------------------------------------------------
# 7. Store Models
# ---------------------------------------------------------

models = {
    "Decision Tree": decision_tree,
    "Bagging": bagging,
    "Random Forest": random_forest,
    "AdaBoost": adaboost,
    "Voting": voting
}

# ---------------------------------------------------------
# 8. Train and Evaluate Models
# ---------------------------------------------------------

results = []

for name, model in models.items():

    print("\n")
    print("=" * 60)
    print(name)
    print("=" * 60)

    # Train
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
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

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    # Store results
    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1
    ])

    # Print Metrics
    print("Accuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)

    print("\nConfusion Matrix:")
    print(cm)

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        y_pred,
        zero_division=0
    ))

    # -----------------------------------------------------
    # Confusion Matrix Plot
    # -----------------------------------------------------

    plt.figure(figsize=(5, 4))

    plt.imshow(cm)

    plt.title(name + " - Confusion Matrix")
    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")

    plt.xticks([0, 1], ["Normal", "Fraud"])
    plt.yticks([0, 1], ["Normal", "Fraud"])

    for i in range(2):
        for j in range(2):
            plt.text(
                j,
                i,
                cm[i, j],
                ha="center",
                va="center"
            )

    plt.colorbar()
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# 9. Final Comparison Table
# ---------------------------------------------------------

result_df = pd.DataFrame(
    results,
    columns=[
        "Algorithm",
        "Accuracy",
        "Precision",
        "Recall",
        "F1"
    ]
)

print("\n")
print("=" * 75)
print("FINAL COMPARISON")
print("=" * 75)

print(result_df.to_string(index=False))

# ---------------------------------------------------------
# 10. Display Percentage Values
# ---------------------------------------------------------

percentage_df = result_df.copy()

percentage_df["Accuracy"] = (
    percentage_df["Accuracy"] * 100
).round(2)

percentage_df["Precision"] = (
    percentage_df["Precision"] * 100
).round(2)

percentage_df["Recall"] = (
    percentage_df["Recall"] * 100
).round(2)

percentage_df["F1"] = (
    percentage_df["F1"] * 100
).round(2)

print("\n")
print("=" * 75)
print("FINAL COMPARISON IN PERCENTAGE")
print("=" * 75)

print(percentage_df.to_string(index=False))

# ---------------------------------------------------------
# 11. Best Model
# ---------------------------------------------------------

best_model = result_df.loc[
    result_df["F1"].idxmax()
]

print("\n")
print("=" * 60)
print("BEST MODEL")
print("=" * 60)

print("Algorithm :", best_model["Algorithm"])
print("Accuracy  :", round(best_model["Accuracy"] * 100, 2), "%")
print("Precision :", round(best_model["Precision"] * 100, 2), "%")
print("Recall    :", round(best_model["Recall"] * 100, 2), "%")
print("F1 Score  :", round(best_model["F1"] * 100, 2), "%")