import numpy as np
import matplotlib.pyplot as plt

def main():
    Score = np.random.randint(100,size=(10,4))
    q1(Score)
    q2(Score)
    q3(Score)
    q4(Score)

def q1(score):
    Y =score[:,0:1]
    X =score[:,1:2]
    plt.plot(X,Y,'^')
    plt.xlabel('English')
    plt.ylabel('Korea')
    plt.show()

def q2(score):
    plt.figure()
    korea = score[:,0:1]
    english = score[:,1:2]
    math = score[:,2:3]
    science = score[:,3:]

    plt.subplot(2,2,1)
    plt.hist(korea)
    plt.xlabel('Korea')
    plt.ylabel('Count')
    plt.subplot(2,2,2)
    plt.hist(english)
    plt.xlabel('English')
    plt.ylabel('Count')
    plt.subplot(2,2,3)
    plt.hist(math)
    plt.xlabel('Math')
    plt.ylabel('Count')
    plt.subplot(2,2,4)
    plt.hist(science)
    plt.xlabel('Science')
    plt.ylabel('Count')
    plt.show()
def q3(score):
    sco = [0,0,0,0]
    a = score[:,0:1]
    b=np.where(a>=90,'A',np.where(a>=80,'B',np.where(a>70,'C','D')))
    for i in b:
        if i =='A':
            sco[0] += 1
        elif i =='B':
            sco[1] += 1
        elif i =='C':
            sco[2] += 1
        else:
            sco[3] += 1
    label =['A','B','C','D']
    plt.pie(sco,labels=label)
    plt.show()


def q4(score):
    plt.boxplot(score)
    plt.xticks([1,2,3,4],['Korea','English','Math','Science'])
    plt.show()

main()