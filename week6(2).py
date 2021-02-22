import keras
import numpy as np
from keras.layers import Dense
from keras.models import Sequential

w = 10
b = 2

X_train = np.array([[0],[1]])
y_train = X_train*w+b

X_test = np.array([[2],[2]])
y_test = X_test*w+b

model = Sequential()

model.add(Dense(2,input_shape=(1,)))
model.summary()

model.complile(loss='mean_squared_error',optimizer='SGD')
model_fit = model.fit(X_train,y_train,batch_size=3,epochs=100,verbose=2)

y_hat = model.predict(X_test)
print(y_hat)
print("Y_Test",y_test)