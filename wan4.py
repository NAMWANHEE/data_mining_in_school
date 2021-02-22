import matplotlib.pylab as plt #데이터를 시각화하기 위해 matplotlib의 패키지에서 pylab을 임포트하고 plt라는 이름으로 대신씀
import numpy as np #벡터형 데이터를 다루기 위해 numpy 패키지를 임포트하고 np라는 이름으로 대신씀
from sklearn.linear_model import LinearRegression #선형회귀를 하기위해 sklearn.linear_model 패키지에 LinearRegression만 임포트하겠다
from sklearn import datasets #데이터를 받아오기위해 sklearn 패키지에서 datasets만 임포트하겠다
from sklearn.model_selection import train_test_split #훈련용/테스트용 데이터로 분리하기위해 sklearn.model_selection패키지에서 train_test_split만 임포트하겠다
diabetes = datasets.load_diabetes() #diabetes라는 변수에 diabetes(당뇨병)데이터를 가져옴
diabetes_X_train = diabetes.data[:-20,:] #diabetes.data는 442X10 크기인데 마지막 20개의 행을뺀 나머지를 diabetes_X_train에 저장 크기는 422X10
diabetes_X_test = diabetes.data[-20:,:] #diabetes.data에서 diabetes_X_train을 뺀 나머지 값을 diabetes_X_test에 저장 크기는 20X10
diabetes_y_train = diabetes.target[:-20] #diabetes.target에서 마지막 20개빼고 나머지를 diabetes_y_train에 저장
diabetes_y_test = diabetes.target[-20:] #diabetes.target에서 마지막 20개만 diabetes_y_test에 저장
model = LinearRegression() #선형회귀분석을 하기위해 model생성
model.fit(diabetes_X_train,diabetes_y_train) #앞서 442X10의 데이터를 이용하여 선형회귀분석을 훈련함
y_pred= model.predict(diabetes_X_test) #diabetes_X_test값을 넣어 y값을 예측
plt.plot(diabetes_y_test,y_pred,'.') #diabetes_y_test,y_pred를 .(점)표시로 그림에 찍어라
x = np.linspace(0,330,100) # 0~330을 100개로 쪼개어 x에 저장
y = x # x의값과 동일
plt.plot(x,y) # x,y의값으로 기울기가 1인 선을 그림
plt.show() #그림으로 보여주기