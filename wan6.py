import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X1 = np.random.randint(101,size=(100,3))
X2 = np.random.randint(50,101,size=(100,3))

y1 = np.zeros(100,dtype =np.int32)
y2 = np.ones(100,dtype =np.int32)
X =np.vstack((X1,X2))
Y =np.vstack((y1,y2)).ravel()

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)
model = LogisticRegression()
model.fit(X_train,Y_train)
pred = model.predict(X_test)
accuracy = accuracy_score(Y_test,pred)

print(pred)
print(accuracy)