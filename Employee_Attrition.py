# Deep Learning Assignment
# Employee Attrition Prediction using MLPClassifier

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ---------------------------------------------------------
# 1. Load Dataset using Pandas
# ---------------------------------------------------------

df = pd.read_csv("Employee_Attrition.csv")

print("Dataset Loaded Successfully")
print("--------------------------------")

# ---------------------------------------------------------
# 2. Display shape, columns and first five records
# ---------------------------------------------------------

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())


# ---------------------------------------------------------
# 3. Check for missing values
# ---------------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())


# ---------------------------------------------------------
# 4. Identify numerical and categorical features
# ---------------------------------------------------------

numerical_features = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_features = df.select_dtypes(include=["object"]).columns.tolist()

print("\nNumerical Features:")
print(numerical_features)

print("\nCategorical Features:")
print(categorical_features)


# ---------------------------------------------------------
# 5. Convert categorical feature OverTime into numerical
# ---------------------------------------------------------

# Yes = 1
# No  = 0

df["OverTime"] = df["OverTime"].map({
    "Yes": 1,
    "No": 0
})

print("\nAfter converting OverTime:")
print(df.head())


# ---------------------------------------------------------
# 6. Convert target Attrition into 0 and 1
# ---------------------------------------------------------

# No  = 0 -> Employee likely to stay
# Yes = 1 -> Employee likely to leave

df["Attrition"] = df["Attrition"].map({
    "No": 0,
    "Yes": 1
})

print("\nTarget values:")
print(df["Attrition"].value_counts())


# ---------------------------------------------------------
# 7. Separate independent and dependent variables
# ---------------------------------------------------------

X = df.drop("Attrition", axis=1)
y = df["Attrition"]

print("\nIndependent Variables:")
print(X.columns.tolist())

print("\nDependent Variable:")
print("Attrition")


# ---------------------------------------------------------
# 8. Divide dataset into training and testing data
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# ---------------------------------------------------------
# 9. Feature Scaling
# ---------------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature scaling completed.")


# ---------------------------------------------------------
# 10. Design MLP with at least two hidden layers
# ---------------------------------------------------------

model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42,
    early_stopping=True,
    validation_fraction=0.1
)


# ---------------------------------------------------------
# 11. Train the network
# ---------------------------------------------------------

model.fit(X_train_scaled, y_train)

print("\nMLP Model Training Completed.")


# ---------------------------------------------------------
# 12. Display number of iterations required
# ---------------------------------------------------------

print("\nNumber of Iterations Required:")
print(model.n_iter_)


# ---------------------------------------------------------
# 13. Calculate Training Accuracy
# ---------------------------------------------------------

train_prediction = model.predict(X_train_scaled)

train_accuracy = accuracy_score(
    y_train,
    train_prediction
)

print("\nTraining Accuracy:")
print(train_accuracy)

print("Training Accuracy Percentage:",
      round(train_accuracy * 100, 2), "%")


# ---------------------------------------------------------
# 14. Calculate Testing Accuracy
# ---------------------------------------------------------

test_prediction = model.predict(X_test_scaled)

test_accuracy = accuracy_score(
    y_test,
    test_prediction
)

print("\nTesting Accuracy:")
print(test_accuracy)

print("Testing Accuracy Percentage:",
      round(test_accuracy * 100, 2), "%")


# ---------------------------------------------------------
# 15. Generate Confusion Matrix
# ---------------------------------------------------------

cm = confusion_matrix(
    y_test,
    test_prediction
)

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(
    y_test,
    test_prediction
))


# ---------------------------------------------------------
# 16. Plot Loss Curve
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    model.loss_curve_
)

plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.grid(True)

plt.show()


# ---------------------------------------------------------
# 17. Create PredictAttrition(employee_data) function
# ---------------------------------------------------------

def PredictAttrition(employee_data):

    # Convert input dictionary to DataFrame

    input_data = pd.DataFrame(
        [employee_data]
    )

    # Convert OverTime
    input_data["OverTime"] = input_data["OverTime"].map({
        "Yes": 1,
        "No": 0
    })

    # Scale input data
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    # Probability
    probability = model.predict_proba(input_scaled)[0]

    if prediction == 1:
        result = "Employee is likely to leave"
    else:
        result = "Employee is likely to stay"

    print("\nPrediction Result:")
    print(result)

    print("Probability of Stay:",
          round(probability[0] * 100, 2), "%")

    print("Probability of Leave:",
          round(probability[1] * 100, 2), "%")

    return prediction


# ---------------------------------------------------------
# 18. Test system using five employee records
# ---------------------------------------------------------

print("\n==========================================")
print("Testing Five Employee Records")
print("==========================================")


for i in range(5):

    employee_data = X.iloc[i].to_dict()

    # Convert OverTime back to Yes/No
    if employee_data["OverTime"] == 1:
        employee_data["OverTime"] = "Yes"
    else:
        employee_data["OverTime"] = "No"

    print("\nEmployee", i + 1)
    print("--------------------------------")

    print(employee_data)

    PredictAttrition(employee_data)


# ---------------------------------------------------------
# 19. Explain Overfitting and Underfitting
# ---------------------------------------------------------

print("\n==========================================")
print("Overfitting and Underfitting Explanation")
print("==========================================")

print("""
Overfitting:
Overfitting occurs when the neural network learns the training
data too closely, including noise. In this case training accuracy
may be very high while testing accuracy is low.

Underfitting:
Underfitting occurs when the model is too simple and cannot learn
the important patterns in the dataset. Both training and testing
accuracy may be low.

In this assignment, feature scaling, early stopping and validation
data are used to reduce the chances of overfitting.
""")