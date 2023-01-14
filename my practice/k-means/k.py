import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# load the data from the CSV file
data = pd.read_csv("km.csv")

# fit the k-means model
kmeans = KMeans(n_clusters=3).fit(data)

# get the cluster centers
centers = kmeans.cluster_centers_

# plot the data points and cluster centers
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['x'], data['y'], data['z'], c=kmeans.labels_)
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], marker='x', c='black')
plt.show()
