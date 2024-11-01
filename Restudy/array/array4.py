# 구간 합 구하기2

import sys

input = sys.stdin.readline

n,m = map(int,input().split()) #차원 배열의 크기
A = [[0]*(n+1)] # A행렬 선언 0으로 초기화
D = [[0]*(n+1) for _ in range(n+1)] #2차원 행렬

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()] #행을 한줄씩 받기 때문에
    A.append(A_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        #합배열 구하기
        D[i][j] = D[i-1][j]+D[i][j-1]-D[i-1][j-1]+A[i][j]

for _ in range(m):
    # 질의에 대한 결과 계산및 출력
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] +D[x1-1][y1-1]
    print(result)