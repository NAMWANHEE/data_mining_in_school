import numpy as np

def andgate(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7

    tmp = np.sum(x*w)+b
    if tmp >0:
        return True
    else:
        return False
print("AND 게이트")
print(andgate(0,1))
print(andgate(1,1))
print('-'*20)
def orgate(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2

    tmp = np.sum(x*w)+b
    if tmp >0:
        return True
    else:
        return False
print("OR 게이트")
print(orgate(0,1))
print(orgate(1,1))

print('-'*20)

def nandgate(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7

    tmp = np.sum(x*w)+b
    if tmp <0:
        return True
    else:
        return False
print("NAND 게이트")
print(nandgate(0,0))
print(nandgate(0,1))
print(nandgate(1,0))
print(nandgate(1,1))

print('-'*20)
def XOR(x1,x2):  #NAND, OR게이트를 AND게이트에 집어넣음
    s1 = nandgate(x1,x2)
    s2 = orgate(x1,x2)
    s3 = andgate(s1,s2)
    return s3
print("XOR 연산")
print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))