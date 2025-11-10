Email Spam Classification Practical – Stepwise Explanation & Revision Notes
Objective
Classify emails as 'Spam' or 'Not Spam' using binary classification. Implement and compare K-Nearest Neighbors (KNN) and Support Vector Machine (SVM) models, analyze data, visualize results, and justify model selection based on performance metrics.

Libraries Used and Their Purpose
pandas: Data loading and manipulation (for reading and exploring the emails dataset).

numpy: Numerical operations, passing vectors to classifiers.

matplotlib & seaborn: Data visualization for quick EDA and interpreting confusion matrix plots.

scikit-learn:

train_test_split: For splitting the dataset into training/testing parts.

StandardScaler: To normalize features (very important for KNN and SVM).

KNeighborsClassifier: K-Nearest Neighbors algorithm.

SVC: Support Vector Machine classifier.

confusion_matrix, classification_report, accuracy_score: For evaluating model performance.

Stepwise Process and Rationale
1. Data Loading and Exploration
Read emails.csv into a DataFrame and check its shape, sample entries, and datatype info.

The dataset has 5172 emails, each characterized by the count of various words (after preprocessing), and a final column 'Prediction' indicating spam (1) or not spam (0).

2. Data Cleaning
Checked for missing values. There were none ().​

Dropped identifier column ('Email No.') and ensured only numeric word-count columns and the target were used.

3. Feature and Target Preparation
Features: All word-count columns except 'Email No.' and 'Prediction'.

Target: 'Prediction' column (1 = spam, 0 = not spam).

4. Train-Test Split
Used a 70:30 split and stratified sampling so both spam/not spam distributions are maintained.

5. Feature Scaling
Applied StandardScaler to ensure all features are on a similar scale.

This is especially critical for KNN (distance-based) and SVM (margin-based) classifiers.

6. K-Nearest Neighbors Classification
Model instantiated with 
k
=
5
k=5.

Trained on scaled data; tested on scaled test set.

KNN Results:

Accuracy: ~82%

Classification report showed Not Spam precision: 0.97, recall: 0.78; Spam precision: 0.63, recall: 0.93. F1-scores indicate good performance on recall for spam, but lower precision for spam.

Confusion matrix:

text
[[856 246]
 [ 31 419]]
Correctly caught 419/450 spam emails, but some non-spam mislabeling (“false positives”).

The model is sensitive to the choice of 
k
k and to scaling.

7. Support Vector Machine Classification
Used a linear kernel.

Excellent performance due to SVM’s strength in handling high-dimensional spaces.

SVM Results:

Accuracy: ~95%

Classification report showed both labels (spam, not spam) at precision and recall values around 0.92–0.97.

Confusion matrix:

text
[[1065  37]
 [ 38 412]]
Very few misclassifications, balanced accuracy and F1-score.

SVM outperformed KNN on this dataset.

8. Performance Comparison and Visualization
SVM accuracy was distinctly better; confusion matrices showed fewer errors and stronger all-around metrics.

Visualized confusion matrix with heatmap for clear interpretation of prediction quality.

Why We Chose SVM
SVM performed better due to its ability to find optimal hyperplanes in high-dimensional, sparse feature sets typical of text/email data.

Higher accuracy and balanced precision/recall for both spam and not-spam classes.

The confusion matrix for SVM had both lower false positives and false negatives compared to KNN.

What Do the Metrics Mean?
Accuracy = Correct predictions / Total predictions.

Precision (per class): Out of all emails predicted as a class, how many are truly of that class.

Recall (per class): Out of all actual emails belonging to a class, how many did the model identify.

F1-Score: Harmonic mean of precision and recall.

Confusion Matrix: Rows = actual; columns = predicted. Diagonal = correct. Off-diagonal = errors (false positives/negatives).

Revision Notes (notes.md)
text
# Email Spam Classification – Revision Notes

## Objective
Classify emails (not spam/spam) using KNN & SVM. Analyze which performs better and why.

## Libraries Used
- pandas/numpy: data handling
- matplotlib/seaborn: visualization
- sklearn: scaling, splitting, classification, evaluation

## Data Cleaning
- No missing values in dataset
- Features: word count columns (skip 'Email No.')
- Target: 'Prediction' (0 = not spam, 1 = spam)

## Splitting & Scaling
- 70% train, 30% test, stratified
- Used StandardScaler on features (critical for KNN/SVM)

## K-Nearest Neighbors (KNN)
- \(k = 5\)
- Accuracy ~82%
- High recall for spam, but lower precision (many non-spam flagged spam)
- Confusion Matrix:
    - True neg (not spam): 856
    - False pos (not spam as spam): 246
    - False neg (spam as not spam): 31
    - True pos (spam): 419

## Support Vector Machine (SVM)
- Linear kernel
- Accuracy ~95%
- Precision, recall, and F1 balanced for both classes
- Fewer false positives/negatives than KNN
- Confusion Matrix:
    - True neg: 1065
    - False pos: 37
    - False neg: 38
    - True pos: 412

## Model Choice
- SVM chosen: Higher accuracy, more balanced precision/recall
- Less susceptible to high dimensionality and scaling issues than KNN

## Important Concepts
- **Confusion matrix**: Table showing correct/incorrect predictions
- **Precision**: Correct positive predictions
- **Recall**: Captured true positives
- **F1 score**: Balance of precision and recall

## Why SVM > KNN here?
- SVM works better for high-dimension, sparse datasets (like term-frequency text)
- Finds the optimal separating margin even with many features

## General EDA
- Checked value distributions, validated absence of missing data


Viva Questions & Answers
1. What is the objective of this experiment?
To classify emails as spam or not spam using KNN and SVM classifiers, evaluate and compare their performance using confusion matrix and classification metrics.

2. Why do we scale features before using KNN and SVM?
Both KNN and SVM rely on distance calculations and margin separation, which are sensitive to feature scales. Scaling ensures that all features contribute equally and prevents bias due to differing units.

3. What is the role of the confusion matrix? Explain its values.
The confusion matrix shows actual vs. predicted classifications, breaking down:

True Positives: Correctly identified spam.

True Negatives: Correctly identified not spam.

False Positives: Non-spam predicted as spam.

False Negatives: Spam predicted as not spam.
Analysis helps diagnose errors and performance between classes.

4. What is precision, recall, and F1 score? Why are they important?
Precision: For predicted positives, how many are actual positives.

Recall: For actual positives, how many were caught by the model.

F1 Score: Harmonic mean of precision and recall; gives a single measure of overall model balance.
They show how well the model copes with class imbalances and prediction errors beyond simple accuracy.

5. What is KNN? Why did you use it for this task?
KNN is a "lazy" classifier that predicts based on the majority label of the k-nearest training samples (using Euclidean or other distances). It is simple, easy to interpret, and effective for baseline comparison, especially on mixed type data.

6. Why did you choose 
k
=
5
k=5 for KNN? Can 
k
k affect performance?
k
=
5
k=5 is a common, default starting point; it helps balance noise (low k) versus overly smooth decision boundaries (high k). The optimal 
k
k can vary depending on dataset and is best chosen using cross-validation.

7. Can you show code to select the best 
k
k in KNN?
Yes! Here is sample code for choosing the best 
k
k using accuracy on the test set:

python
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

k_values = list(range(1, 21))
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_pred = knn.predict(X_test_scaled)
    accuracies.append(accuracy_score(y_test, y_pred))

plt.plot(k_values, accuracies, marker='o')
plt.xlabel('k value')
plt.ylabel('Test Accuracy')
plt.title('KNN Accuracy for different k values')
plt.show()
This lets you visually inspect and pick the 
k
k with highest accuracy (or use cross-validation for reliability).

8. What is SVM? Why is it good for email spam detection?
Support Vector Machine finds the optimal separating hyperplane in high-dimensional feature space, which is especially useful for text/email data after vectorization. SVMs are robust to "curse of dimensionality" and good at handling sparse features typical in spam detection with word counts.

9. Why did SVM perform better than KNN?
SVM leverages geometric margins and works better in high-dimensional data, producing higher accuracy (fewer errors) whereas KNN is more affected by noise, feature scaling, and local data density.

10. If you saw class imbalance, what would you do?
Consider using stratified sampling on split, evaluation using precision/recall/F1 per class, or try oversampling/undersampling (SMOTE) or class-weighted SVM for better balance.

11. What preprocessing steps did you take before classification?
Dropped identifier columns.

Ensured only numeric features.

Checked and handled missing values.

Applied scaling to features.

Your plot of "KNN Accuracy for different k values" clearly shows how the performance changes as 
k
k increases. At low 
k
k (k=1,2,3), the accuracy is highest (above 0.85), and as 
k
k increases, the test accuracy drops off steadily, falling below 0.7 at k=20.

What does this plot mean?
Best k value:
The highest accuracy is achieved at low values of 
k
k, especially 
k
=
1
k=1 or 
k
=
2
k=2.
In practice, 
k
=
5
k=5 is often used as a starting point for a balance between overfitting (very low 
k
k) and underfitting (very high 
k
k), but for your dataset and split, a lower 
k
k is optimal.

Overfitting vs. Underfitting:
Lower 
k
k: High sensitivity to noise, potentially overfits.
Higher 
k
k: More "smoothing," may underfit and miss detail in the structure.

Viva Answer:
"We selected 
k
=
5
k=5 as a reasonable starting value, but we validated our choice by plotting the accuracy for a range of 
k
k. The graph showed that lower 
k
k values gave better accuracy in this dataset, so using k=1,2, or 3 would actually maximize accuracy here. The optimal k should be chosen empirically for each dataset using such plots or cross-validation."

What should you say if asked about this in viva?
"We experimented with different values of 
k
k and plotted their test accuracy. The graph showed accuracy is highest for small 
k
k, especially k=1, and declines as 
k
k increases. Therefore, for this dataset, selecting small 
k
k values is statistically justified. The reason is smaller 
k
ks are more sensitive to the local data distribution, while larger k dilute the decision and may underfit minority instances."

Extra Notes for Revision/Viva
Why not always pick k=1?
k=1 is very sensitive to noise and may not generalize well if there's mislabeled or outlier data. Often, a small odd number (k=3,5) is chosen for balance.

How to select k systematically?

Use the plot of accuracy vs. k (as you did).

Use cross-validation (GridSearchCV in sklearn) to automate k selection.

Can you improve KNN further?

Try weighting neighbors by distance (weights='distance' in KNeighborsClassifier).

Remove outliers or noisy points in preprocessing.

This visualization is a strong demonstration for viva responses—refer to your plot and explain your choice confidently!

Screenshot_20251110_230738.jpg

Your screenshot confirms 