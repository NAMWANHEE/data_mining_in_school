import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

height_weight = np.loadtxt('heights.csv',delimiter=',')
x=np.array(height_weight[:,0]).reshape(-1,1)
y=np.array(height_weight[:,1]).reshape(-1,1)
line_fitter = LinearRegression()
line_fitter.fit(x,y)
y_predicted = line_fitter.predict(x)
plt.plot(x,y,'o')
plt.plot(x,y_predicted)
print("기울기: ",line_fitter.coef_)
print("y 절편: ",line_fitter.intercept_)
plt.xlabel('height')
plt.ylabel('weight')
plt.show()