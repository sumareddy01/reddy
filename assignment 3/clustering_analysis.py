import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_circles, make_blobs
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering


def plot_clusters(X, labels, title):
    plt.figure(figsize=(6, 4))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolor='k')
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.tight_layout()
    filename = f"{title.replace(' ', '_').lower()}.png"
    plt.savefig(filename)
    plt.close()
    print(f"Saved plot: {filename}")


def run_clustering():
    datasets = {
        "Moons": make_moons(noise=0.05, random_state=0),
        "Circles": make_circles(noise=0.05, factor=0.5, random_state=1),
        "Blobs": make_blobs(random_state=2)
    }

    for name, (X, _) in datasets.items():
        # KMeans
        kmeans = KMeans(n_clusters=2, random_state=0)
        kmeans_labels = kmeans.fit_predict(X)
        plot_clusters(X, kmeans_labels, f"{name} - KMeans Clustering")

        # Hierarchical
        hier = AgglomerativeClustering(n_clusters=2)
        hier_labels = hier.fit_predict(X)
        plot_clusters(X, hier_labels, f"{name} - Hierarchical Clustering")

        # DBSCAN
        dbscan = DBSCAN(eps=0.2)
        dbscan_labels = dbscan.fit_predict(X)
        plot_clusters(X, dbscan_labels, f"{name} - DBSCAN Clustering")


if __name__ == "__main__":
    run_clustering()
