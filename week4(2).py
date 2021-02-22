from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
import numpy as np

iris = load_iris()
idx=np.in1d(iris.target,[0,2])

x=iris.data[idx,:2]
y=(iris.target[idx]/2).astype(np.int)

model = Perceptron().fit(x,y)