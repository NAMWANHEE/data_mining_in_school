import numpy as np
def main():
    a = np.empty((10, 1))
    Score = np.random.randint(100,size=(10,4))
    q1(Score)
    q2(Score)
    q3(Score,a)
    q4(Score,a)

def q1(score):
    print("문제 1")
    b=np.where(score>=90,'A',np.where(score>=80,'B',np.where(score>=70,'C','D')))
    print(b)

def q2(score):
    print("문제 2")
    mean=score.mean(axis=0)
    c=score-mean
    print(c)
def q3(score,a):
    print("문제 3")
    for i in range(10):
        a[i]=sum(score[i,:])
    print(np.hstack((score,a)).astype(np.int))

def q4(score,a):
    print("문제 4")
    mean = score.mean(axis=1)
    b = mean.reshape(10,1)
    c=np.hstack((score,a,b))
    d = c.mean(axis=0)
    e =np.vstack((c,d))
    print(e)



main()
