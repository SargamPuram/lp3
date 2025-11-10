1. Problem Definition
2. collection
preparation
da
building
evaluation
deployment

General Machine Learning & Data Science Interview Questions and Answers
1. What is the Data Science Lifecycle?
Problem Understanding: Define the business or research problem.

Data Collection: Gather data from databases, APIs, sensors, etc.

Data Cleaning: Handle missing values, outliers, inconsistencies.

Exploratory Data Analysis (EDA): Visualize and understand data patterns and relationships.

Feature Engineering: Create or transform variables to improve model performance.

Model Selection: Choose appropriate ML algorithms based on problem.

Training: Fit model to training data.

Evaluation: Use metrics like accuracy, precision, recall, F1-score, RMSE, etc.

Deployment: Integrate model into production workflow.

Monitoring: Track and maintain model performance over time.

2. What is Error and Accuracy in ML?
Accuracy: Proportion of correct predictions among total predictions.

Error: Measures like Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE) quantify prediction deviation from true values.

Accuracy is intuitive for classification; errors suit regression.

3. What are common Python libraries and their primary uses?
pandas: Data manipulation and preprocessing.

numpy: Numerical computing.

matplotlib / seaborn: Data visualization.

scikit-learn: ML algorithms, preprocessing, evaluation metrics.

scipy: Scientific computing, hierarchical clustering, statistics.

4. Briefly explain these ML algorithms discussed:
K-Nearest Neighbors (KNN): Classifies based on majority label among k closest points in feature space; simple, lazy learner.

Support Vector Machine (SVM): Finds optimal hyperplane separating classes; potent in high-dimensional spaces.

Regression Models: Predict continuous targets; linear regression assumes linear relationship; random forest regression combines many decision trees to model complex patterns.

K-Means Clustering: Unsupervised learning to partition data into k clusters by minimizing intra-cluster distances.

Hierarchical Clustering: Builds tree-like cluster hierarchy; can visualize via dendrogram.

5. What is a confusion matrix?
A table displaying True Positives, False Positives, True Negatives, and False Negatives to evaluate classification performance including errors per class.

6. Explain Bagging and Boosting (ensemble methods)
Bagging (Bootstrap Aggregation): Combines multiple independent models trained on bootstrapped data samples; reduces variance and avoids overfitting. Example: Random Forest.

Boosting: Sequentially builds models that try to correct errors of previous ones by adjusting sample weights; reduces bias and variance. Examples: AdaBoost, Gradient Boosting, XGBoost.

7. How do bagging and boosting differ?
Bagging parallelizes model training; boosting trains sequentially.

Bagging focuses on variance reduction; boosting tackles both bias and variance.

Boosting can overfit if not regulated; bagging is more robust.