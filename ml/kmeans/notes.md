K-Means Clustering Practical - Detailed Explanation & Notes
Objective
Group sales data entries into clusters using K-Means and Hierarchical clustering. Identify the optimal number of clusters using the Elbow method and interpret clustering results with plots.

Libraries Used and Their Uses
pandas, numpy: For data loading, cleaning, and numeric operations

matplotlib, seaborn: Data visualization such as scatter plots, heatmaps, dendrograms

scikit-learn:

StandardScaler: Normalize feature scales before clustering

KMeans: Perform K-Means clustering

scipy.cluster.hierarchy:

linkage and dendrogram: Perform and visualize hierarchical clustering

fcluster: Extract clusters from dendrogram cutting

Stepwise Procedure
1. Load and Inspect Data
Loaded sales_data_sample.csv with pandas.read_csv.

Explored shape, data types, and checked for missing values.

Found data clean with numeric features suitable for clustering.

2. Exploratory Data Analysis (EDA)
Plotted distribution histogram for Sales to understand skewness or spread.

Created scatter plot of MSRP (Manufacturer's Suggested Retail Price) vs Sales to capture relationship patterns and possible clusters.

Visualized correlation heatmap among numeric features to understand feature interrelations and redundancy.

3. Data Preprocessing
Selected only numeric columns for clustering.

Applied StandardScaler for feature scaling to remove bias and ensure proper Euclidean distances in clustering.

4. Elbow Method to Determine Optimal k
Ran K-Means for 
k
=
1
 to 
10
k=1 to 10.

Plotted Within-Cluster-Sum-of-Squares (WCSS) against k.

Identified the elbow point 
k
=
3
k=3, where inertia reduction slows, suggesting optimal cluster count.

5. K-Means Clustering
Fit K-Means with chosen 
k
=
3
k=3.

Assigned cluster labels back to original dataframe.

Visualized clusters on a scatter plot (first two numeric features), color-coded by cluster.

Included cluster centroids on the same plot to understand cluster centers.

6. Hierarchical Clustering
Generated linkage matrix using Ward's method.

Plotted dendrogram for hierarchical relationships between data points.

Cut dendrogram at 3 clusters and labeled data accordingly.

Visualized hierarchical clusters similarly to K-Means.

Plot Interpretations
Sales Histogram: Showed distribution skewed right, indicating many low sales values and some high-value outliers.

MSRP vs Sales Scatter: Indicated clusters may form due to policy/price points and sales volumes. Clustering aims to group such patterns.

Correlation Heatmap:
Revealed strong positive correlations among pricing and sales features, confirming relatedness of features used in clustering.

KMeans Scatter with Centroids:
Visual clear separation into 3 distinct clusters with centroids marking average cluster positions in scaled feature space.

Dendrogram:
Showed hierarchical structuring of data points and justified choice of 3 clusters by height cut.

Summary Notes (notes.md)
text
# K-Means Clustering Practical Notes

## Objective
Cluster sales data and find optimal cluster count using Elbow method and Hierarchical clustering.

## Libraries
- pandas, numpy: data handling
- matplotlib, seaborn: visualization
- sklearn: StandardScaler, KMeans clustering
- scipy.cluster: hierarchical clustering

## Data Handling
- Loaded dataset; no missing values
- Selected numeric columns for clustering
- Scaled features for fair distance measurements

## EDA
- Sales histogram: skewed distribution
- MSRP vs Sales scatter: potential cluster structure
- Correlation heatmap: feature interrelations

## Clustering
- Elbow method: WCSS plot to find optimal k = 3
- KMeans fit with k=3; clusters assigned and visualized
- Dendrogram plot for hierarchical clustering with 3 clusters

## Interpretation
- Clusters reveal natural groupings in sales and price pattern
- Centroids represent average cluster feature values
- Hierarchical clusters confirm KMeans groups

## Usefulness
- Helps marketing/sales strategy, inventory management by customer segmentation
- Understand patterns and anomalies in sales data

Viva Questions & Answers: K-Means Clustering Practical
What is the objective of this practical?
To group sales data samples into distinct clusters using K-Means and Hierarchical clustering, determine optimal cluster count using the elbow method, and visualize the clusters.

Which libraries have you used and why?

pandas, numpy: For data loading and manipulation.

matplotlib, seaborn: For plotting distributions, scatterplots, heatmaps, and dendrograms.

scikit-learn: For scaling features and K-Means clustering.

scipy.cluster: For hierarchical clustering and dendrogram visualization.

What data cleaning/preprocessing did you do?
Dropped missing values, selected numeric columns only for clustering, and applied StandardScaler to normalize features to similar scales essential for distance-based methods.

What did the elbow method tell you?
The elbow plot of WCSS (Within-Cluster Sum of Squares) vs number of clusters showed a clear bend at k=3, indicating that 3 clusters explain the data well without unnecessary complexity.

Explain K-Means algorithm briefly? Why did you use it here?
K-Means partitions data into k clusters by minimizing intra-cluster variance. It is simple, scalable, and effective for grouping similar data points, making it ideal for sales data segmentation.

What does the cluster centroid represent?
The centroid is the mean position of all points in a cluster, representing its center in feature space. It summarizes cluster characteristics.

What did the scatter plots reveal?
The MSRP vs Sales scatter plot, color-coded by clusters, shows natural separations and helps interpret what differentiates clusters based on these sales features.

What is a dendrogram? What did you learn from it?
A dendrogram visualizes hierarchical clustering by showing nested cluster merges at various distances. Cutting the dendrogram at a height gave 3 clusters, consistent with the elbow method for K-Means.

Why do we scale data before clustering?
Because clustering methods are distance-based and features on different scales may dominate distance calculations, scaling ensures equal contribution.

How can clustering results help businesses?
Segmentation can identify customer groups or product categories for targeted marketing, inventory optimization, and personalized strategies.