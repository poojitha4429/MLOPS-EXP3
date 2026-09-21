"""
Iris Flower Classification using Random Forest
==============================================
College Lab Assignment - Git and DVC Demo
Author: Manasa
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# ─────────────────────────────────────────────
# HYPERPARAMETERS — Version 2
# ─────────────────────────────────────────────
N_ESTIMATORS = 200   # Number of trees in the forest
MAX_DEPTH    = 15    # Maximum depth of each tree
RANDOM_STATE = 42    # Seed for reproducibility
MODEL_VERSION = "Version 2"

# ─────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────
DATA_PATH    = "data/iris.csv"
MODEL_PATH   = "models/random_forest.pkl"
METRICS_PATH = "results/metrics.txt"

# ─────────────────────────────────────────────
# STEP 1: Load Dataset
# ─────────────────────────────────────────────
print("=" * 50)
print(f"  Random Forest Classifier - {MODEL_VERSION}")
print("=" * 50)

df = pd.read_csv(DATA_PATH)
print(f"\n[1] Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"    Species distribution:\n{df['Species'].value_counts().to_string()}")

# ─────────────────────────────────────────────
# STEP 2: Separate Features and Target
# ─────────────────────────────────────────────
X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = df['Species']

print(f"\n[2] Features: {list(X.columns)}")
print(f"    Target: Species ({y.nunique()} classes)")

# ─────────────────────────────────────────────
# STEP 3: Train/Test Split (80% train, 20% test)
# ─────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)
print(f"\n[3] Train/Test Split:")
print(f"    Training samples : {len(X_train)}")
print(f"    Testing  samples : {len(X_test)}")

# ─────────────────────────────────────────────
# STEP 4: Train Random Forest Classifier
# ─────────────────────────────────────────────
print(f"\n[4] Training Random Forest...")
print(f"    n_estimators = {N_ESTIMATORS}")
print(f"    max_depth    = {MAX_DEPTH}")
print(f"    random_state = {RANDOM_STATE}")

model = RandomForestClassifier(
    n_estimators=N_ESTIMATORS,
    max_depth=MAX_DEPTH,
    random_state=RANDOM_STATE
)
model.fit(X_train, y_train)
print("    Training complete!")

# ─────────────────────────────────────────────
# STEP 5: Evaluate Model
# ─────────────────────────────────────────────
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"\n[5] Model Evaluation:")
print(f"    Accuracy: {accuracy * 100:.2f}%")
print(f"\n    Classification Report:")
print(report)

# ─────────────────────────────────────────────
# STEP 6: Save Model
# ─────────────────────────────────────────────
os.makedirs("models", exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"[6] Model saved to: {MODEL_PATH}")

# ─────────────────────────────────────────────
# STEP 7: Save Metrics
# ─────────────────────────────────────────────
os.makedirs("results", exist_ok=True)
with open(METRICS_PATH, "w") as f:
    f.write(f"Random Forest Classifier - {MODEL_VERSION}\n")
    f.write("=" * 50 + "\n")
    f.write(f"Dataset        : {DATA_PATH}\n")
    f.write(f"Dataset rows   : {df.shape[0]}\n")
    f.write(f"n_estimators   : {N_ESTIMATORS}\n")
    f.write(f"max_depth      : {MAX_DEPTH}\n")
    f.write(f"random_state   : {RANDOM_STATE}\n")
    f.write(f"Train samples  : {len(X_train)}\n")
    f.write(f"Test samples   : {len(X_test)}\n")
    f.write(f"Accuracy       : {accuracy * 100:.2f}%\n")
    f.write("\nClassification Report:\n")
    f.write(report)

print(f"[7] Metrics saved to: {METRICS_PATH}")
print(f"\n{'=' * 50}")
print(f"  DONE — Accuracy: {accuracy * 100:.2f}%")
print(f"{'=' * 50}\n")
