
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Mall_Customers.csv')

print(df.shape)
print(df.head())

x = df.iloc[:,[3,4]].values
print(x.shape)

from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters = i, init = 'k-means++', max_iter=300, n_init= 10, random_state = 0)
    km.fit(x)
    wcss.append(km.inertia_)

plt.plot(range(1,11), wcss)
plt.title('Elbow method', fontsize=20)
plt.xlabel('No of Clusters')
plt.ylabel("wcss")
plt.show()





km = KMeans(n_clusters = 5, init = 'k-means++', max_iter=300, n_init= 10, random_state = 0)
y_means = km.fit_predict(x)

plt.rcParams['figure.figsize'] = (15,8)
plt.style.use('fivethirtyeight')

plt.scatter(x[y_means == 0,0],x[y_means == 0,1], s=100 , c='pink', label = 'general')
plt.scatter(x[y_means == 1,0] ,x[y_means == 1,1], s=100 , c='yellow', label ='spendtrift')
plt.scatter(x[y_means == 2,0] ,x[y_means == 2,1], s= 100 ,c='cyan', label ='target')
plt.scatter(x[y_means == 3,0] ,x[y_means == 3,1], s=100, c='magenta' ,label = 'careful')
plt.scatter(x[y_means == 4,0] ,x[y_means == 4,1], s=100 ,c='orange' , label = 'miser')

plt.style.use('fivethirtyeight')
plt.title('K_Means_Clustering',fontsize = 20)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.grid()
plt.show()



