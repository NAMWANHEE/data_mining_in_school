import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
np.random.seed(100)
x = np.random.randn(100,1) * 10
y = 5+ x + np.random.randn(100,1)

line_fitter = LinearRegression()
line_fitter.fit(x,y)
y_predicted = line_fitter.predict(x)
a = line_fitter.coef_
print(a)
b = line_fitter.intercept_
print(b)
plt.plot(x,y,'o')
plt.plot(x,y_predicted)
plt.show()

