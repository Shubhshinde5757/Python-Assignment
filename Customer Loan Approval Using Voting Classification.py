# ============================================================
# Machine Learning Assignment
# Customer Loan Approval Using Voting Classification
# ============================================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


# ============================================================
# 1. Load the Dataset
# ============================================================

df = pd.read_csv("Loan_Default.csv")

print("========== DATASET ==========")
print(df)

print("\nDataset Shape:")
print(df.shape)


# ============================================================
# 2. Check for Missing Values
# ============================================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# ============================================================
# 3. Separate Input and Output Variables
# ============================================================

# Dataset मध्ये Default column आहे.
# Assignment मध्ये target column LoanApproved आहे.
#
# Default = 0  --> Loan Approved = 1
# Default = 1  --> Loan Approved = 0

df["LoanApproved"] = 1 - df["Default"]


# Input variables
X = df.drop(["Default", "LoanApproved"], axis=1)

# Output variable
y = df["LoanApproved"]


print("\n========== INPUT VARIABLES ==========")
print(X.head())

print("\n========== OUTPUT VARIABLE ==========")
print(y.head())


# ============================================================
# 4. Split Dataset into Training and Testing Data
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n========== TRAIN TEST SPLIT ==========")

print("Training Data:", X_train.shape)
print("Testing Data :", X_test.shape)


# ============================================================
# Preprocessing
# ============================================================

# Categorical columns
categorical_columns = [
    "PreviousDefault",
    "HomeOwnership"
]

# Numerical columns
numerical_columns = [
    "Age",
    "Income",
    "LoanAmount",
    "CreditScore",
    "EmploymentYears",
    "ExistingLoans",
    "MonthlyDebt",
    "LoanTerm"
]


# ------------------------------------------------------------
# Preprocessing for Logistic Regression and KNN
# ------------------------------------------------------------

scaled_preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numerical_columns
        ),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ]
)


# ------------------------------------------------------------
# Preprocessing for Decision Tree
# ------------------------------------------------------------

tree_preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            "passthrough",
            numerical_columns
        ),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ]
)


# ============================================================
# 5. Train Logistic Regression
# ============================================================

logistic_regression = Pipeline(
    steps=[
        (
            "preprocessor",
            scaled_preprocessor
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                random_state=42
            )
        )
    ]
)

logistic_regression.fit(
    X_train,
    y_train
)

lr_prediction = logistic_regression.predict(
    X_test
)

lr_accuracy = accuracy_score(
    y_test,
    lr_prediction
)

print("\n========== LOGISTIC REGRESSION ==========")
print("Accuracy:",
      lr_accuracy)

print("Accuracy Percentage:",
      lr_accuracy * 100, "%")


# ============================================================
# 6. Train Decision Tree
# ============================================================

decision_tree = Pipeline(
    steps=[
        (
            "preprocessor",
            tree_preprocessor
        ),
        (
            "classifier",
            DecisionTreeClassifier(
                random_state=42
            )
        )
    ]
)

decision_tree.fit(
    X_train,
    y_train
)

dt_prediction = decision_tree.predict(
    X_test
)

dt_accuracy = accuracy_score(
    y_test,
    dt_prediction
)

print("\n========== DECISION TREE ==========")
print("Accuracy:",
      dt_accuracy)

print("Accuracy Percentage:",
      dt_accuracy * 100, "%")


# ============================================================
# 7. Train KNN
# ============================================================

knn = Pipeline(
    steps=[
        (
            "preprocessor",
            scaled_preprocessor
        ),
        (
            "classifier",
            KNeighborsClassifier(
                n_neighbors=5
            )
        )
    ]
)

knn.fit(
    X_train,
    y_train
)

knn_prediction = knn.predict(
    X_test
)

knn_accuracy = accuracy_score(
    y_test,
    knn_prediction
)

print("\n========== KNN ==========")
print("Accuracy:",
      knn_accuracy)

print("Accuracy Percentage:",
      knn_accuracy * 100, "%")


# ============================================================
# 8. Individual Model Accuracies
# ============================================================

print("\n========== INDIVIDUAL ACCURACIES ==========")

print(
    "Logistic Regression :",
    round(lr_accuracy * 100, 2),
    "%"
)

print(
    "Decision Tree       :",
    round(dt_accuracy * 100, 2),
    "%"
)

print(
    "KNN                 :",
    round(knn_accuracy * 100, 2),
    "%"
)


# ============================================================
# 9. Create Hard Voting Classifier
# ============================================================

hard_voting = VotingClassifier(
    estimators=[
        ("lr", logistic_regression),
        ("dt", decision_tree),
        ("knn", knn)
    ],
    voting="hard"
)

hard_voting.fit(
    X_train,
    y_train
)

hard_prediction = hard_voting.predict(
    X_test
)

hard_accuracy = accuracy_score(
    y_test,
    hard_prediction
)

print("\n========== HARD VOTING CLASSIFIER ==========")

print(
    "Hard Voting Accuracy:",
    hard_accuracy
)

print(
    "Hard Voting Accuracy Percentage:",
    round(hard_accuracy * 100, 2),
    "%"
)


# ============================================================
# 10. Calculate Hard Voting Accuracy
# ============================================================

print("\nHard Voting Accuracy:",
      round(hard_accuracy * 100, 2),
      "%")


# ============================================================
# 11. Create Soft Voting Classifier
# ============================================================

soft_voting = VotingClassifier(
    estimators=[
        ("lr", logistic_regression),
        ("dt", decision_tree),
        ("knn", knn)
    ],
    voting="soft"
)

soft_voting.fit(
    X_train,
    y_train
)

soft_prediction = soft_voting.predict(
    X_test
)

soft_accuracy = accuracy_score(
    y_test,
    soft_prediction
)

print("\n========== SOFT VOTING CLASSIFIER ==========")

print(
    "Soft Voting Accuracy:",
    soft_accuracy
)

print(
    "Soft Voting Accuracy Percentage:",
    round(soft_accuracy * 100, 2),
    "%"
)


# ============================================================
# 12. Calculate Soft Voting Accuracy
# ============================================================

print("\nSoft Voting Accuracy:",
      round(soft_accuracy * 100, 2),
      "%")


# ============================================================
# 13. Compare All Models
# ============================================================

comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],

    "Accuracy": [
        lr_accuracy,
        dt_accuracy,
        knn_accuracy,
        hard_accuracy,
        soft_accuracy
    ]
})


# Accuracy percentage
comparison["Accuracy (%)"] = (
    comparison["Accuracy"] * 100
)


print("\n")
print("================================================")
print("              FINAL COMPARISON")
print("================================================")

print(
    comparison[
        ["Model", "Accuracy (%)"]
    ].to_string(index=False)
)


# ============================================================
# Find Best Model
# ============================================================

best_model = comparison.loc[
    comparison["Accuracy"].idxmax()
]

print("\n================================================")
print("BEST MODEL")
print("================================================")

print(
    "Best Model:",
    best_model["Model"]
)

print(
    "Best Accuracy:",
    round(best_model["Accuracy (%)"], 2),
    "%"
)


# ============================================================
# End
# ============================================================

print("\nAssignment Completed Successfully!")