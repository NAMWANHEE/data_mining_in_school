import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
a = pd.DataFrame(iris.data,columns=iris.feature_names)
a['target'] = iris.target
a['targetName'] = np.where(a['target'] ==0,"setosa",np.where(a['target'] == 1,"versicolor","virginica"))
print(a.head())

plt.figure()
one =a.iloc[:,:2][a.target ==0]
two =a.iloc[:,:2][a.target ==1]
three =a.iloc[:,:2][a.target ==2]
plt.plot(one['sepal length (cm)'],one['sepal width (cm)'],'or',label='setosa')
plt.plot(two['sepal length (cm)'],two['sepal width (cm)'],'xb',label='versicolor')
plt.plot(three['sepal length (cm)'],three['sepal width (cm)'],'^g',label='virginica')
plt.legend()
plt.xlabel('sepal length')
plt.ylabel("sepal width")
plt.figure()
one1 =a.iloc[:,2:4][a.target ==0]
two1 =a.iloc[:,2:4][a.target ==1]
three1 =a.iloc[:,2:4][a.target ==2]
plt.plot(one1['petal length (cm)'],one1['petal width (cm)'],'or',label='setosa')
plt.plot(two1['petal length (cm)'],two1['petal width (cm)'],'xb',label='versicolor')
plt.plot(three1['petal length (cm)'],three1['petal width (cm)'],'^g',label='virginica')
plt.legend()
plt.xlabel('petal length')
plt.ylabel("petal width")
plt.show()