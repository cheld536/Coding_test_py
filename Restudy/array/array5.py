# 나머지 합 구하기 p.50
# 입력 값은 5 3 / 1 2 3 1 2  예시 출력 : 7
# c[i] 나머지 인덱스 개수에서 2가지를 뽑는 경우의 수 공식은 c[i] * (c[i]-1)/2

import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # n,m의 입력
A = list(map(int,input().split())) #배열 선언
S = [0] *n #합 배열 선언
S[0] = A[0] #합 배열 S[0]은 A[0]과 동일하다
C = [0] *n #나머지 합을 찾는 배열 선언
answer = 0 #답을 저장할 변수

for i in range(1,n):
    S[i] = S[i-1] +A[i]  #합배열 저장

for i in range(n):
    remainder = S[i] % m
    if(remainder == 0):     # 만약 합 배열 %m 한 나머지의 값이 0이면 S[i]와S[j]는 같다
       answer += 1
    C[remainder] += 1

for i in range(m):
    #나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if C[i]>1:
        answer += (C[i]*(C[i]-1)//2) # / -> 하면 float 형이 됨 , // 나누고 몫 만 취한다.



print(answer)