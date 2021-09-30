import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics

# Read in the file and fill all null spaces with mean scores
df = pd.read_csv("CC.csv")
df = df.fillna(df.mean())

# Generate the x with the features
X = df.drop(['CUST_ID', 'TENURE'], axis=1)
# Set Tenure to the target
y = df['TENURE']

# Set clusters to KMean then fit the data
nclusters = 2 # this is the k in kmeans
km = KMeans(n_clusters=nclusters, random_state=0)
km.fit(X)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X)
# Find the silhouette score
score = metrics.silhouette_score(X, y_cluster_kmeans)
print(score)

##elbow method to know the number of clusters
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

