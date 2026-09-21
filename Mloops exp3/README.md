# Iris Flower Classification using Random Forest with Git and DVC

## Project Overview
This project demonstrates Machine Learning version control using:
- **Git** for source code versioning
- **DVC (Data Version Control)** for dataset and model versioning

## Dataset
The classic Iris dataset — 150 samples of iris flowers with 4 features:
- Sepal length, Sepal width, Petal length, Petal width
- Target: Iris species (Setosa, Versicolor, Virginica)

## ML Model
**Random Forest Classifier** from scikit-learn
- Version 1: n_estimators=100, max_depth=10, random_state=42
- Version 2: n_estimators=200, max_depth=15, random_state=42

## Project Structure
```
Git-DVC-ML-Project/
├── data/
│   └── iris.csv            # Dataset (tracked by DVC)
├── src/
│   └── train.py            # Training script
├── models/
│   └── random_forest.pkl   # Trained model (tracked by DVC)
├── results/
│   └── metrics.txt         # Accuracy and metrics
├── .gitignore
├── requirements.txt
├── README.md
└── EXPERIMENT_REPORT.md
```

## Setup Instructions
```bash
# Install dependencies
pip install -r requirements.txt

# Pull dataset and model from DVC remote
dvc pull

# Train the model
python src/train.py
```

## Tools Used
| Tool | Purpose |
|------|---------|
| Python 3.12 | Programming language |
| pandas | Data manipulation |
| scikit-learn | Machine learning |
| joblib | Model serialization |
| Git | Source code versioning |
| DVC | Data and model versioning |
| GitHub | Remote Git repository |

## College Lab Assignment
Demonstrates Git + DVC workflow for reproducible machine learning experiments.
