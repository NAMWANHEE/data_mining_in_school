import numpy as np
def main():
    Score = np.random.randint(100,size=(10,4))
    q1(Score)
    q2(Score)
    q3(Score)
    q4(Score)

def q1(score):
    print("모든 학생의 수학 점수")
    print(score[:,2:3]) #1번

def q2(score):
    print("각 학생의 총 합 점수")
    for i in range(10): #2번
        print(sum(score[i,:]))
def q3(score):
    print("불린인덱스를 이용하여 1,5,7,9,10 번째 학생의 과목")
    a =[True,False,False,False,True,False,True,False,True,True]
    print(score[a]) # 3번
def q4(score):
    print("10*4 행렬을 4*10 으로 변경")
    b= score.transpose((1,0)) #4번
    print(b)
main()

