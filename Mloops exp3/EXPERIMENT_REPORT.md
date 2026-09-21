# Experiment Report
## Iris Flower Classification using Random Forest with Git and DVC

---

## 1. Project Title
**Iris Flower Classification using Random Forest with Git and DVC**

---

## 2. Objective
To demonstrate a complete Machine Learning version control workflow using:
- **Git** for source code versioning
- **DVC (Data Version Control)** for dataset and model versioning
- **GitHub** as the remote Git repository
- **Local DVC remote storage** for dataset and model storage

The project shows how to track multiple versions of datasets and ML models,
restore previous versions, and reproduce experiments from scratch.

---

## 3. Tools Used

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.12.2 | Programming language |
| pandas | 2.2.2 | Data loading and manipulation |
| scikit-learn | 1.5.1 | Random Forest Classifier |
| joblib | 1.4.2 | Model serialization (.pkl) |
| Git | 2.49.0 | Source code version control |
| DVC | 3.51.2 | Dataset and model versioning |
| GitHub | - | Remote Git repository |
| Local folder | - | DVC remote storage |

---

## 4. Project Structure

```
Mloops exp3/                        <- Project root (Git repo)
├── data/
│   ├── iris.csv                    <- Dataset (tracked by DVC, ignored by Git)
│   └── iris.csv.dvc                <- DVC metadata pointer (tracked by Git)
├── src/
│   └── train.py                    <- Training script (tracked by Git)
├── models/
│   ├── random_forest.pkl           <- Trained model (tracked by DVC, ignored by Git)
│   └── random_forest.pkl.dvc       <- DVC metadata pointer (tracked by Git)
├── results/
│   └── metrics.txt                 <- Accuracy results (tracked by Git)
├── .dvc/
│   └── config                      <- DVC remote configuration
├── .gitignore                      <- Excludes data/model binaries from Git
├── requirements.txt                <- Python dependencies
├── README.md                       <- Project overview
└── EXPERIMENT_REPORT.md            <- This file
```

---

## 5. Git Setup

- Initialized Git repository: `git init`
- Created GitHub repository: `https://github.com/manasakv123/git-dvc-ml-project`
- Added remote: `git remote add origin <url>`
- Branch: `main`
- Total commits: 8

### Git Commit History

| Commit | Message |
|--------|---------|
| f46f983 | Initial ML project setup |
| edfbc80 | Initialize DVC |
| df53c9f | Add Iris dataset with DVC |
| 4a9c8ad | Configure local DVC remote storage |
| 4015bc0 | Update dataset to version 2 - added 6 new rows (156 total) |
| bd1bada | Add training script and Model Version 1 metrics (Accuracy: 87.50%) |
| ada463e | Add Random Forest model version 1 (Accuracy: 87.50%, n_estimators=100, max_depth=10) |
| 95aabcd | Update Random Forest model to version 2 (n_estimators=200, max_depth=15, Accuracy: 87.50%) |

---

## 6. DVC Setup

- Initialized DVC: `dvc init`
- DVC creates `.dvc/` configuration folder and `.dvcignore`
- DVC metadata files (`.dvc`) are committed to Git
- Actual data/model files are stored in DVC remote storage

### DVC Remote Configuration
```
[core]
    remote = localstorage
[remote "localstorage"]
    url = C:\Users\manas\OneDrive\Desktop\dvc-storage
```

---

## 7. Dataset Description

**Name:** Iris Flower Dataset  
**Source:** Classic UCI Machine Learning Repository dataset  
**Format:** CSV  

### Features
| Column | Description | Unit |
|--------|-------------|------|
| Id | Row identifier | - |
| SepalLengthCm | Length of sepal | cm |
| SepalWidthCm | Width of sepal | cm |
| PetalLengthCm | Length of petal | cm |
| PetalWidthCm | Width of petal | cm |
| Species | Target class | - |

### Target Classes
- Iris-setosa
- Iris-versicolor
- Iris-virginica

---

## 8. Dataset Version 1

| Property | Value |
|----------|-------|
| Rows | 150 |
| Samples per class | 50 each |
| DVC MD5 hash | 77638d3f356111872605458eb6151444 |
| File size | 5,258 bytes |
| Git commit | df53c9f |
| Commit message | Add Iris dataset with DVC |

---

## 9. Dataset Version 2

| Property | Value |
|----------|-------|
| Rows | 156 |
| Samples per class | 52 each |
| Change | Added 6 new valid rows (2 per species) |
| DVC MD5 hash | 21efc502231b617281ef8122a2b31cc1 |
| File size | 5,470 bytes |
| Git commit | 4015bc0 |
| Commit message | Update dataset to version 2 - added 6 new rows (156 total) |

---

## 10. Dataset Restoration Process

To restore Dataset Version 1 from Version 2:

```bash
# Step 1: Restore V1 metadata from Git history
git checkout df53c9f -- data/iris.csv.dvc

# Step 2: DVC fetches actual V1 file from remote storage
dvc checkout

# Step 3: Verify (should show 150 rows)
python -c "import pandas as pd; df=pd.read_csv('data/iris.csv'); print('Rows:', len(df))"

# Step 4: Return to Version 2
git checkout main -- data/iris.csv.dvc
dvc checkout
```

**Why it works:** DVC stores each version of the file using its MD5 hash as the filename
in remote storage. When we point the `.dvc` file to the old hash, DVC retrieves exactly
that version.

---

## 11. Random Forest Model — Version 1

| Property | Value |
|----------|-------|
| Algorithm | RandomForestClassifier (scikit-learn) |
| Dataset | Dataset Version 2 (156 rows) |
| n_estimators | 100 |
| max_depth | 10 |
| random_state | 42 |
| Train samples | 124 (80%) |
| Test samples | 32 (20%) |
| **Accuracy** | **87.50%** |
| Model file size | 159,153 bytes |
| DVC MD5 hash | d5ad1952ac0d585fdbbaffa996b2b392 |
| Git commit | ada463e |

### Classification Report — Model V1
```
              precision    recall  f1-score   support
 Iris-setosa       1.00      1.00      1.00        10
Iris-versicolor    0.77      0.91      0.83        11
 Iris-virginica    0.89      0.73      0.80        11
    accuracy                           0.88        32
```

---

## 12. Random Forest Model — Version 2

| Property | Value |
|----------|-------|
| Algorithm | RandomForestClassifier (scikit-learn) |
| Dataset | Dataset Version 2 (156 rows) |
| n_estimators | 200 |
| max_depth | 15 |
| random_state | 42 |
| Train samples | 124 (80%) |
| Test samples | 32 (20%) |
| **Accuracy** | **87.50%** |
| Model file size | 317,169 bytes |
| DVC MD5 hash | 435a1097d732821b10119038e4ee04ba |
| Git commit | 95aabcd |

### Classification Report — Model V2
```
              precision    recall  f1-score   support
 Iris-setosa       1.00      1.00      1.00        10
Iris-versicolor    0.77      0.91      0.83        11
 Iris-virginica    0.89      0.73      0.80        11
    accuracy                           0.88        32
```

---

## 13. Experiment Results Comparison Table

| Version | Dataset | n_estimators | max_depth | random_state | Accuracy | Model Size |
|---------|---------|-------------|-----------|--------------|----------|------------|
| Model V1 | Dataset V2 (156 rows) | 100 | 10 | 42 | **87.50%** | 159,153 bytes |
| Model V2 | Dataset V2 (156 rows) | 200 | 15 | 42 | **87.50%** | 317,169 bytes |

> **Note:** Both models achieve the same accuracy on this small, balanced dataset.
> However, Model V2 is a larger and more complex model (200 trees vs 100 trees, nearly
> double the file size). DVC correctly identifies them as different versions through
> their MD5 hashes. In real-world projects with larger datasets, hyperparameter changes
> typically produce different accuracy values.

---

## 14. Model Restoration Process

To restore Model Version 1 from Version 2:

```bash
# Step 1: Restore V1 metadata from Git history
git checkout ada463e -- models/random_forest.pkl.dvc

# Step 2: DVC fetches actual V1 binary from remote storage
dvc checkout models/random_forest.pkl.dvc

# Step 3: Verify (should show n_estimators=100, max_depth=10)
python -c "import joblib; m=joblib.load('models/random_forest.pkl'); print(m.n_estimators, m.max_depth)"

# Step 4: Return to Version 2
git checkout main -- models/random_forest.pkl.dvc
dvc checkout models/random_forest.pkl.dvc
```

---

## 15. Reproducibility Test

A fresh clone of the repository was made into a separate folder:
`Git-DVC-ML-Project-Reproduced/`

### Steps performed on cloned repo:

```bash
# Clone from GitHub (gets code + .dvc metadata only, NO data/model)
git clone https://github.com/manasakv123/git-dvc-ml-project.git

# Pull dataset and model from DVC remote
dvc pull
# Output: A data\iris.csv  |  A models\random_forest.pkl  |  2 files added

# Run training
python src/train.py
# Output: Accuracy: 87.50%  (identical to original)
```

### Results matched exactly:
| Property | Original | Cloned |
|----------|----------|--------|
| Dataset rows | 156 | 156 |
| n_estimators | 200 | 200 |
| max_depth | 15 | 15 |
| Accuracy | 87.50% | 87.50% |

**Conclusion:** The project is fully reproducible. ✅

---

## 16. Git vs DVC Comparison

| Feature | Git | DVC |
|---------|-----|-----|
| **Code versioning** | ✅ Excellent — designed for text/code files, full diff support | ⚠️ Not intended for code |
| **Dataset versioning** | ⚠️ Can track small files but inefficient for large CSVs; no diff for binary | ✅ Designed for large files; stores by MD5 hash; efficient deduplication |
| **Model versioning** | ⚠️ Can store .pkl files but bloats repo; no semantic diff | ✅ Ideal — stores binary model files efficiently outside Git |
| **Collaboration** | ✅ GitHub/GitLab for code sharing, branching, PRs | ✅ Shared remote storage (S3, GDrive, local) for data sharing |
| **Reproducibility** | ✅ Pins exact code version via commit hash | ✅ Pins exact data/model version via MD5 hash; `dvc pull` restores files |

> **Important clarification:** Git CAN technically track any file including datasets
> and models. However, it becomes impractical for large binary files because:
> (1) GitHub has a 100MB file size limit, (2) binary files cannot be meaningfully
> diffed, (3) every version is stored in full making the repo very large.
> DVC is specifically designed to solve these problems while staying connected
> to Git commits.

---

## 17. Conclusion

This project successfully demonstrated:

1. **Git initialization** and GitHub remote setup for code versioning
2. **DVC initialization** and local remote storage configuration
3. **Dataset versioning** — two versions of iris.csv tracked with DVC
4. **Dataset restoration** — Version 1 (150 rows) restored from Version 2 (156 rows)
5. **Model training** — Random Forest classifier with documented hyperparameters
6. **Model versioning** — two model versions tracked with DVC
7. **Model restoration** — Version 1 (100 trees) restored from Version 2 (200 trees)
8. **Reproducibility** — fresh clone + `dvc pull` + `python src/train.py` produced
   identical results (87.50% accuracy)

The combination of **Git + DVC** provides a complete, lightweight, and reproducible
Machine Learning version control system without requiring expensive cloud storage.

---

*Report generated for College Lab Assignment — Git and DVC*  
*Author: Manasa*  
*Date: September 2026*
