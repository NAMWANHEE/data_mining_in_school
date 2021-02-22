import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import pandas as pd

#과적합(overfitting)
# students ={'hours':[29,9,10,38,16,26,50,10,30,33,43,2,39,15,44,29,41,15,24,50],
#            'test_result':[65,7,8,76,23,56,100,3,74,48,73,0,62,37,74,40,90,42,58,100]}
# student_data = pd.DataFrame(data=students)
# x = student_data.hours
# y = student_data.test_result
# X_train = x[0:12]
# y_train = y[0:12]
# X_test = x[12:]
# y_test = y[12:]
#
# def polynomial_fit(degree=1):
#     return np.poly1d(np.polyfit(X_train,y_train,degree))
# def plot_polyfit(degree=1):
#     p = polynomial_fit(degree)
#     plt.scatter(X_train,y_train,label="Training set")
#     plt.scatter(X_test,y_test,label="Test set")
#     curve_x= np.arange(min(x),max(x),0.01)
#     plt.plot(curve_x,p(curve_x),label="Polynomial of degree {}".format(degree))
#
#     print(r2_score(y,p(x)))
#     plt.legend()
#     plt.plot()
# plt.subplot(2,2,1)
# plot_polyfit(1)
# plt.subplot(2,2,2)
# plot_polyfit(2)
# plt.subplot(2,2,3)
# plot_polyfit(5)
# plt.subplot(2,2,4)
# plot_polyfit(7)
# plt.show()

#2
label_dict = {'M':0,'B':1}
dataset = pd.read_csv('./cancer.csv')
dataset = dataset.drop('id',axis=1)
dataset ['diagnosis'] = dataset['diagnosis'].map(label_dict)
dataset.shape